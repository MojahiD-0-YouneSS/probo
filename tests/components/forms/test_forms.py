from src.probo.components.forms import (
    ProboForm,
    ProboFormField,
)

# ==============================================================================
#  TEST: Declarative Forms (No Django / Manual Mode)
# ==============================================================================

def test_declarative_form_style_1_variables():
    """
    Type I: Define fields as variables first, then pass to Form.
    """
    # 1. Define Fields
    username_field = ProboFormField(
        tag_name="input",
        field_label="Hello",
        name="username",
        value="258246413",
        Type="text",
        placeholder="Enter Name",
    )

    bio_field = ProboFormField(
        tag_name="textarea",
        field_label="Bio",
        content="Hello from earth",
        name="bio",
        # Textarea content usually passed as value or content depending on implementation
        # Assuming MFF handles value as content for textarea
    )

    password_field = ProboFormField(
        tag_name="input", field_label="Enter Password", name="password", Type="password"
    )

    # 2. Initialize Form with variables
    # We pass fields as *args (implied by your syntax) or a list
    form = ProboForm(
        "/contact/submit/",
        username_field,
        bio_field,
        password_field,
        method="POST",
        csrf_token="manual-token-87566462464",
    )
    # 3. Render
    html = form.render()
    # 4. Verify
    # Container
    assert '<form action="/contact/submit/" method="post"' in html
    assert 'value="manual-token-87566462464"' in html

    # Username
    assert "<label>Hello</label>" in html
    assert 'value="258246413"' in html
    assert 'name="username"' in html

    # Bio (Textarea)
    assert "<textarea" in html
    assert ">Hello from earth</textarea>" in html

    # Password
    assert 'type="password"' in html

def test_declarative_form_style_2_inline():
    """
    Type II: Define fields directly inside the Form constructor (Inline).
    """
    form = ProboForm(
        "/save/",
        ProboFormField(
            tag_name="input",
            field_label="Age",
            name="age",
            value="25",
            Type="number",
        ),
        ProboFormField(
            tag_name="input",
            field_label="I Agree",
            name="agree",
            Type="checkbox",
            checked=True,
        ),
        # Field 1: Input
        method="post",
        csrf_token="token-xyz-999",
    )

    html = form.render()

    # Verify Form
    assert 'action="/save/"' in html
    assert 'value="token-xyz-999"' in html

    # Verify Inline Fields
    assert 'type="number"' in html
    assert 'value="25"' in html
    assert 'type="checkbox"' in html
    assert "checked" in html

# ... (Previous imports and tests) ...

# ==============================================================================
#  TESTS: Declarative Builder API (MFF.add_*)
# ==============================================================================

def test_mff_builder_input():
    """
    Test add_input builder method.
    Should render Label + Input.
    """
    # Initialize generic/empty MFF
    # Assuming MFF init allows defaults or we pass a dummy tag that gets overridden
    mff = ProboFormField()

    # Configure via builder
    mff.add_input(
        label_string="Email Address",
        label_attrs={"for": "user_email"},
        Type="email",
        Id="user_email",
        value="test@example.com",
        name="email",
        placeholder="john@doe.com",  # extra attr
        required=True,  # extra attr
    )

    html = mff.render()

    assert '<label for="user_email">Email Address</label>' in html
    assert "<input" in html
    assert 'type="email"' in html
    assert 'id="user_email"' in html
    assert 'value="test@example.com"' in html
    assert 'placeholder="john@doe.com"' in html
    assert "required" in html

def test_mff_builder_textarea():
    """
    Test add_textarea builder method.
    Should render Label + Textarea (content inside tags).
    """
    mff = ProboFormField()

    mff.add_textarea(
        textarea_content="This is my story.",
        label_string="Biography",
        label_attrs={"for": "bio_id"},
        Id="bio_id",
        name="bio",
        rows=5,
    )

    html = mff.render()

    assert '<label for="bio_id">Biography</label>' in html
    assert "<textarea" in html
    assert 'id="bio_id"' in html
    assert 'rows="5"' in html
    assert ">This is my story.</textarea>" in html

def test_mff_builder_select_simple():
    """
    Test add_select_option with a simple list of values.
    """
    mff = ProboFormField()

    options = ["Red", "Green", "Blue"]
    # Select index 1 (Green)
    mff.add_select_option(
        option_values=options,
        selected_options_indexes=[1],
        label_string="Pick a Color",
        label_attrs={"for": "color_select"},
        name="colors",
        Id="color_select",
        size=1,
    )

    html = mff.render()

    assert "<select" in html
    assert 'name="colors"' in html
    # Option 0 (Red) - Not selected
    assert '<option value="Red">Red</option>' in html
    # Option 1 (Green) - Selected
    assert '<option value="Green" selected>Green</option>' in html

def test_mff_builder_select_optgroup():
    """
    Test add_select_optgroup for grouped options.
    """
    mff = ProboFormField()

    groups = {"Fruits": ["Apple", "Banana"], "Vegetables": ["Carrot", "Potato"]}

    # Assume flattening index: 0=Apple, 1=Banana, 2=Carrot. Let's select Carrot (2)
    # (Implementation dependent on how you index groups, adjusting test to verify structure)
    mff.add_select_optgroup(
        optgroups=groups,
        selected_options_indexes=[],  # No selection for this test
        label_string="Category",
        label_attrs={"for": "food_select"},
        name="food",
        Id="food_select",
        size=1,
    )

    html = mff.render()

    assert '<optgroup label="Fruits">' in html
    assert '<option value="Apple">Apple</option>' in html
    assert '<optgroup label="Vegetables">' in html
    assert '<option value="Carrot">Carrot</option>' in html

def test_mff_builder_fieldset():
    """
    Test add_field_set rendering a container with legend and nested elements.
    """
    mff = ProboFormField()

    # Pre-rendered child elements to go inside
    child_inputs = ['<input name="child1">', '<input name="child2">']

    mff.add_field_set(
        legend_content="User Information",
        form_elements=child_inputs,
        label_string="Group Label",
        label_attrs={"for": "user_group"},
        name="user_group",
    )

    html = mff.render()

    assert "<fieldset" in html
    assert "<legend>User Information</legend>" in html
    assert '<input name="child1">' in html
    # Verify nesting order
    assert html.index("<legend>") < html.index("<input")

def test_mff_builder_datalist():
    """
    Test add_data_list for autocomplete suggestions.
    """
    mff = ProboFormField()

    options = ["Chrome", "Firefox", "Safari"]

    mff.add_data_list(
        option_value_list=options,
        label_string="Browser List",
        Id="browsers",
    )

    html = mff.render()

    assert '<datalist id="browsers">' in html
    assert (
        '<option value="Chrome"></option>' in html
    )  # Datalist options usually self-closing or empty content
    assert "</datalist>" in html

def test_mff_builder_output():
    """
    Test add_output element.
    """
    mff = ProboFormField()

    mff.add_output(
        label_string="Total:",
        name="result",
        For="a b",  # Calculation based on inputs a and b
    )

    html = mff.render()

    assert "<output" in html
    assert 'name="result"' in html
    assert 'for="a b"' in html
    assert "Total:" in html
