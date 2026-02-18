def base_template():
    """Generates the primary HTML shell and boilerplate for a ProboUI application.

    This function acts as the "Master Layout" or "Main Entry Point" for the 
    application's DOM structure. It demonstrates the integration of three 
    core ProboUI pillars:
    1.  **Tag Functions**: Programmatic generation of HTML (head, body, nav, etc.).
    2.  **HTMX Integration**: Declarative AJAX and partial DOM updates using `HX()` 
        and `HXE()`.
    3.  **Bootstrap 5 Styling**: JIT-resolved utility classes via `BS5ElementStyle`.

    The template includes standard SEO meta tags, Bootstrap 5 CSS/JS CDN links, 
    and a responsive navigation bar as a default structural example.

    Detailed Workflow:
        - **Head Generation**: Configures viewport, charset, and external assets.
        - **Navigation Bar**: Constructs a responsive Bootstrap navbar using 
          nested functional tags.
        - **HTMX Trigger**: Includes an example of a `span` element utilizing 
          HTMX for dynamic content swapping via `HXE()`.
        - **Serialization**: Wraps the final output in a `Template` object 
          marked as the system base.

    Returns:
        Template: A ProboUI Template object loaded with the serialized HTML 
            and the necessary DOCTYPE declaration.
    """
    
    from probo.components.tag_functions import (
        meta,
        link,
        title,
        style,
        nav,
        script,
        div,
        button,
        span,
        a,
        ul,
        li,
        head,
        body,
        html,
        doctype,
    )
    from probo.htmx.htmx import HTMX as HX, HTMXElement as HXE

    from probo.styles.frameworks import (
        BS5ElementStyle,
    )

    # head block

    head_string = head(
        meta(
            charset="UTF-8",
        ),
        meta(
            http_equiv="x-ua-compatible",
            content="ie=edge",
        ),
        meta(
            name="viewport",
            content="width=device-width, initial-scale=1.0",
        ),
        meta(
            name="description",
            content="Behold My Awesome Project!",
        ),
        meta(
            name="author",
            content="Jon Doe",
        ),
        title(
            "my project",
            "is cool",
        ),
        link(
            rel="icon",
            href="images/favicons/favicon.ico",
        ),
        link(
            rel="stylesheet",
            href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.2.3/css/bootstrap.min.css",
            integrity="sha512-SbiR/eusphKoMVVXysTKG/7VseWii+Y3FdHrt0EpKgpToZeemhqHeZeLWLhJutz/2ut2Vw1uQEj2MbRF+TVBUA==",
            crossorigin="anonymous",
            referrerpolicy="no-referrer",
        ),
        style(),
        HX().get_script_tag(),
        script(
            src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.2.3/js/bootstrap.min.js",
            integrity="sha512-1/RvZTcCDEUjY/CypiMz+iqqtaoQfAITmNSJY17Myp4Ms5mdxPS5UV7iOfdZoxcGhzFbOm6sntTKJppjvuhg4g==",
            crossorigin="anonymous",
            referrerpolicy="no-referrer",
        ),
        script(src="js/project.js"),
    )
    # body
    body_string = body(
        div(
            nav(
                div(
                    button(
                        span(
                            Class="navbar-toggler-icon",
                        ),
                        Class="navbar-toggler navbar-toggler-right"
                        + BS5ElementStyle("button").add("display_block").render(),
                        type="button",
                    ),
                    a("mvp_base", Class="navbar-brand", href="/home"),
                    div(
                        ul(
                            li(
                                a(
                                    span("home", Class="visually-hidden"),
                                    Class="nav-link active",
                                    href="/home",
                                ),
                                Class="nav-item",
                            ),
                            li(
                                a(
                                    "about",
                                    Class="nav-link",
                                    href="/about",
                                ),
                                Class="nav-item",
                            ),
                            li(
                                a(
                                    "log in",
                                    Id="log-in-link",
                                    Class="nav-link",
                                    href="/account_login",
                                ),
                                Class="nav-item",
                            ),
                            Class="navbar-nav mr-auto",
                        ),
                        Class="collapse navbar-collapse",
                        Id="navbarSupportedContent",
                    ),
                    Class="container-fluid",
                ),
                Class="navbar navbar-expand-md navbar-light bg-light",
            ),
            Class="mb-1",
        ),
        div(
            span(
                "click me",
                style="font-size:100px; color:green;",
                **HXE()
                .set_attr(
                    get="/contact",
                    trigger="click",
                    target="#navbarSupportedContent",
                    swap="innerHTML",
                )
                .render(as_string=False),
            ),
            Class="container",
        ),
        script(""),
    )
    html_string = html(head_string, body_string, lang="en")
    from probo.components.elements import (
        Template as TMPLT,
    )

    return TMPLT().load_base_template(doctype(html_string), use_as_base=True)
