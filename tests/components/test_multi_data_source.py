from probo import DIV, H1, SPAN
from probo.components.conf import settings


def test_data_pipeline_separation():
    # 1. Define the Global UI State (Dynamic Data)
    global_app_state = {
        "current_user": "Youness",
        "theme": "dark",
        "secret_token": "abc-123"
    }
    settings.WELCOME_HEADING1 = "Welcome to Probo UI"
    settings.WELCOME_SPAN = "HELLO"
    # 2. Build the Component Tree
    # We pass the dynamic data to the ROOT node.
    app = DIV(
        # Static content mixed with Dynamic bindings {'theme'}
        H1({'WELCOME_HEADING1'}, data_pipeline=settings,Class={'theme'}),

        # This child needs 'current_user' from the parent's dynamic pipeline
        SPAN({"WELCOME_SPAN"}, {'current_user'},{'secret_token'}),

        data_pipeline=global_app_state,
    )
    # 3. Apply Data Policies (Simulating a secure backend lock)
    # Protect the secret token so children (like the SPAN) cannot access it
    app.provide_data("secret_token", "abc-123", policy="pri")

    # 4. Trigger the resolution traverse (simulating the framework's pre-render phase)
    app.resolve_pipeline_variables(swap_vars=True)
    for child in app.walk():
        if hasattr(child, 'resolve_pipeline_variables'):
            child.resolve_pipeline_variables(swap_vars=True)
# 5. Render output
    html = str(app.render())

    # ---------------------------------------------------------
    # 6. ROBUST ASSERTIONS
    # ---------------------------------------------------------

    # A. Test Local Pipeline Resolution (H1 -> settings)
    assert "Welcome to Probo UI" in html, "FAILED: H1 did not resolve variables from its local data_pipeline (settings)."

    # B. Test Ancestor Tree Climbing for Attributes (H1 -> DIV)
    # The H1 must climb up to the DIV to find the 'theme' key for its class.
    assert 'class="dark"' in html or "class='dark'" in html, "FAILED: H1 did not climb the tree to resolve the 'theme' attribute from the parent DIV."

    # C. Test Ancestor Tree Climbing for Content (SPAN -> DIV)
    assert "Youness" in html, "FAILED: SPAN did not climb the tree to resolve 'current_user' from the parent DIV."

    # D. Test Sibling Isolation & Missing Variables (strict_data=False)
    # SPAN asks for 'WELCOME_SPAN', but that lives in 'settings' attached to the H1.
    # Siblings do not share pipelines. It should fail to resolve and be swapped with "".
    assert "HELLO" not in html, "FAILED: SPAN inappropriately accessed a sibling's isolated data pipeline."
    assert "{'WELCOME_SPAN'}" not in html, "FAILED: Unresolved variables were not correctly swapped with empty strings."

    # E. Test Data Policy Security (NodeDataPolicy.PRIVATE)
    # The SPAN tries to render 'secret_token', but it is marked private on the parent.
    # It must be blocked by the depth check (_depth > 0) in the mixin's get_data method.
    # 1. Test Sibling Isolation
    assert "HELLO" not in html, "FAILED: SPAN inappropriately accessed a sibling's isolated data pipeline."

    # 2. Test Security Policy
    assert "abc-123" not in html, "CRITICAL SECURITY FAILURE: Private data leaked to a child node!"