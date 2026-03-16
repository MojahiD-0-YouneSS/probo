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
from probo.components.tag_classes import (
    META,
    LINK,
    TITLE,
    STYLE,
    NAV,
    SCRIPT,
    DIV,
    BUTTON,
    SPAN,
    A,
    UL,
    LI,
    HEAD,
    BODY,
    HTML,
    DOCTYPE,
    H1, 
    H2,
    P,
    SECTION,
    MAIN, 
    FOOTER,
)
from probo.htmx.htmx import HTMX as HX, HTMXElement as HXE
from typing import Any


def base_template_string(head_list:list[str]|None=None,body_list:list[str]|None=None, overide_head:bool=False,overide_body:bool=False,base_title='My Project')->str:
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
    
        DOCTYPE (Root)
        └── HTML [lang="en"]
            ├── HEAD
            │   ├── META [charset="UTF-8"]
            │   ├── META [http-equiv="x-ua-compatible"]
            │   ├── META [viewport]
            │   ├── META [description]
            │   ├── META [author]
            │   ├── TITLE ("my project is cool")
            │   ├── LINK [favicon]
            │   ├── LINK [bootstrap.css]
            │   ├── STYLE
            │   ├── SCRIPT [htmx.js]
            │   ├── SCRIPT [bootstrap.js]
            │   └── SCRIPT [project.js]
            └── BODY
                ├── DIV [Class="mb-1"] (Navbar Wrapper)
                │   └── NAV [Class="navbar..."]
                │       └── DIV [Class="container-fluid"]
                │           ├── BUTTON (Navbar Toggler)
                │           │   └── SPAN [Class="navbar-toggler-icon"]
                │           ├── A [Class="navbar-brand"] ("mvp_base")
                │           └── DIV [Id="navbarSupportedContent"] (Collapse)
                │               └── UL [Class="navbar-nav mr-auto"]
                │                   ├── LI -> A ("home")
                │                   ├── LI -> A ("about")
                │                   └── LI -> A ("log in")
                ├── DIV [Class="container"] (Main Content Container)
                │   └── SPAN [hx-get="/contact"] ("click me")
                └── SCRIPT ("")
    Args:
        head_list: type list[str] a list of head safe elements to be passed to head section.
        body_list: type list[str] a list of body safe elements to be passed to body section.
        overide_head: type bool if True, the default head block will not be rendered and only the head_list elements will be rendered in the head section.
        overide_body: type bool if True, the default body block will not be rendered and only the body_list elements will be rendered in the body section.
        base_title: type str the title for the HTML document.
    Returns:
        Template: A ProboUI Template object loaded with the serialized HTML 
            and the necessary DOCTYPE declaration.
    """
    if overide_head and not head_list:
        head_list=[]
    if overide_body and not body_list:
        body_list=[]
    # head block
    if not overide_head:
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
                base_title,
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
    else:
        head_string = head(*head_list)
    # body
    if overide_body:
        body_string = body(*body_list)
    else:
        body_string = body()

    html_string = html(head_string, body_string, lang="en")

    return doctype(html_string)

def base_template_tree(head_nodes:list[Any]|None=None,body_nodes:list[Any]|None=None, overide_head:bool=False,overide_body:bool=False) -> DOCTYPE:
    """Generates the primary HTML tree shell and boilerplate for a ProboUI application.

    This function acts as the "Master Layout" or "Main Entry Point" for the
    application's DOM structure. It demonstrates the integration of three
    core ProboUI pillars:
    1.  **Tag Functions**: Programmatic generation of HTML (head, body, nav, etc.).
    2.  **HTMX Integration**: Declarative AJAX and partial DOM updates using `HX()`
        and `HXE()`.
    3.  **Bootstrap 5 Styling**: JIT-resolved utility classes via `BS5ElementStyle`.

    The template includes standard SEO meta tags, Bootstrap 5 CSS/JS CDN links,
    and a responsive navigation bar as a default structural example.
    Args:
        head_nodes: a list of head safe node elements to be passed to head section.
        body_nodes: a list of body safe node elements to be passed to body section.
        overide_head: type bool if True, the default head block will not be rendered and only the head_nodes elements will be rendered in the head section.
        overide_body: type bool if True, the default body block will not be rendered and only the body_nodes elements will be rendered in the body section.

    Detailed Workflow:
        - **Head Generation**: Configures viewport, charset, and external assets.
        - **Navigation Bar**: Constructs a responsive Bootstrap navbar using
          nested functional tags.
        - **HTMX Trigger**: Includes an example of a `span` element utilizing
          HTMX for dynamic content swapping via `HXE()`.
        - **Serialization**: Wraps the final output in a `Template` object
          marked as the system base.

        
    BASE_TEMPLATE_TREE_MAP :
    DOCTYPE (Root)
    └── HTML [lang="en"]
        ├── HEAD
        │   ├── META [charset="UTF-8"]
        │   ├── META [http-equiv="x-ua-compatible"]
        │   ├── META [viewport]
        │   ├── META [description]
        │   ├── META [author]
        │   ├── TITLE ("my project is cool")
        │   ├── LINK [favicon]
        │   ├── LINK [bootstrap.css]
        │   ├── STYLE
        │   ├── SCRIPT [htmx.js]
        │   ├── SCRIPT [bootstrap.js]
        │   └── SCRIPT [project.js]
        └── BODY

    Returns:
        Template: A ProboUI Template object loaded with the serialized HTML
            and the necessary DOCTYPE declaration.
    """
    if overide_head and not head_nodes:
        head_nodes = []
    if overide_body and not body_nodes:
        body_nodes = []

    # head block
    head_obj = HEAD()
    if not overide_head:
        head_obj.add(META(
                charset="UTF-8",
            ))
        head_obj.add(META(
                http_equiv="x-ua-compatible",
                content="ie=edge",
            ))
        head_obj.add(META(
                name="viewport",
                content="width=device-width, initial-scale=1.0",
            ))
        head_obj.add(META(
                name="description",
                content="Behold My Awesome Project!",
            ))
        head_obj.add(META(
                name="author",
                content="Jon Doe",
            ))
        head_obj.add(TITLE(
                "my project",
            ))
        head_obj.add(LINK(
                rel="icon",
                href="images/favicons/favicon.ico",
            ))
        head_obj.add(LINK(
                rel="stylesheet",
                href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.2.3/css/bootstrap.min.css",
                integrity="sha512-SbiR/eusphKoMVVXysTKG/7VseWii+Y3FdHrt0EpKgpToZeemhqHeZeLWLhJutz/2ut2Vw1uQEj2MbRF+TVBUA==",
                crossorigin="anonymous",
                referrerpolicy="no-referrer",
            ))
        head_obj.add(STYLE())
        head_obj.add(SCRIPT(src=HX().htmx_cdn_url))
        head_obj.add(SCRIPT(
                src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.2.3/js/bootstrap.min.js",
                integrity="sha512-1/RvZTcCDEUjY/CypiMz+iqqtaoQfAITmNSJY17Myp4Ms5mdxPS5UV7iOfdZoxcGhzFbOm6sntTKJppjvuhg4g==",
                crossorigin="anonymous",
                referrerpolicy="no-referrer",
            ))
        head_obj.add(SCRIPT(src="js/project.js"))
    else:
        for node in head_nodes: head_obj.add(node)
    # body
    body_obj = BODY()
    if overide_body:
        for node in body_nodes:
            body_obj.add(node)
    html_obj = HTML( lang="en")
    html_obj.add(head_obj).add(body_obj)
    return DOCTYPE(html_obj)

def welcome_template_tree():
    
    """
    DOCTYPE (Root)
    └── HTML [lang="en"]
        ├── HEAD (Inherited from base_template_tree)
        │   └── STYLE (Custom .elephant-launch & .card-link animations)
        └── BODY
            └── MAIN [style="min-height: 100vh; ..."]
                ├── SECTION (Hero Section)
                │   └── DIV [style="text-align: center; ..."]
                │       ├── SPAN ("🐘") [animation="float 3s..."]
                │       ├── H1 ("The install worked successfully!")
                │       └── P ("You are seeing this page because...")
                ├── SECTION (Documentation Links)
                │   └── DIV [style="display: grid; ..."]
                │       ├── A ("Documentation") -> H2, P
                │       ├── A ("Tutorial") -> H2, P
                │       └── A ("Community") -> H2, P
                └── FOOTER (Status Bar)
                    └── DIV [style="border-top: 1px solid..."]
                        └── P ("Probo UI v1.3.0 — 800+ Tests Passed")
    """
    from probo.styles import element_style

    LAUNCH_STYLE = """
    @keyframes float {
        0% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-20px) rotate(2deg); }
        100% { transform: translateY(0px) rotate(0deg); }
    }
    .card-link {
        transition: all 0.3s ease;
        text-decoration: none;
        color: #1A5F7A;
        border: 1px solid #e2e8f0;
    }
    .card-link:hover {
        background: #f8fafc;
        border-color: #1A5F7A;
        transform: scale(1.02);
    }
    """
    elephant_launch=element_style(
        with_style_attr=True,
        font_size= '120px',
        display= 'inline-block',
        animation= 'float 3s ease-in-out infinite',
        filter= 'drop-shadow(0 10px 15px rgba(0,0,0,0.1))',
    )
    hero_section_style=element_style(
        with_style_attr=True,
        background= '#fff',
        border_bottom= '1px solid #eee',
        )
    hero_container_style = element_style(
        with_style_attr=True,
        padding= '60px 20px',
        text_align= 'center',
    )
    hero_paragraph_style = element_style(
        with_style_attr=True,
        color= '#666',
        font_size= '18px',
        max_width= '600px',
        margin= '20px auto',
    )
    hero_heading_style = element_style(
        with_style_attr=True,
        font_size= '32px',
        color= '#333',
        margin_top= '20px',
    )
    documentation_section_style = element_style(
        with_style_attr=True,
        padding= '0 60px 20px',
    )
    documentation_container_style = element_style(
        with_style_attr=True,
        display='grid',
        grid_template_columns='repeat(auto-fit, minmax(250px, 1fr))',
        gap='20px',
        max_width='1000px',
        margin='-40px auto 0'
    )
    documentation_link_style = element_style(
        with_style_attr=True,
        padding= '30px',
        border_radius= '12px',
        display= 'block',
    )
    documentation_link_heading_style = element_style(
        with_style_attr=True,
        font_size= '20px',
        margin_bottom= '10px',
    )
    documentation_link_paragraph_style = element_style(
        with_style_attr=True,
        font_size= '14px',
        color= '#64748b',
    )
    footer_section = element_style(
        with_style_attr=True,
        padding= '40px',
        text_align= 'center',
        color= '#94a3b8',
        border_top= '1px solid #f1f5f9',
    )
    footer_paragraph_status= element_style(
        with_style_attr=True,
        font_weight= 'bold',
    )
    main_section_style = element_style(
        with_style_attr=True,
        min_height= '100vh',
        background= '#fcfcfc',
        font_family= 'system-ui, -apple-system, sans-serif',
    )
    def HeroSection():
        """The centerpiece of the landing page."""
        return SECTION(
            DIV(
                SPAN("🐘", **elephant_launch),
                H1(
                    "The install worked successfully! Congratulations!",
                    **hero_heading_style,
                ),
                P(
                    "You are seeing this page because <b>DEBUG = True</b> is in your settings and you have not yet configured any pages.",
                    **hero_paragraph_style,
                ),
                **hero_container_style,
            ),
            **hero_section_style,
        )

    def DocumentationLinks():
        """The link grid for the Probo ecosystem."""
        links = [
            {
                "title": "Documentation",
                "desc": "Comprehensive guides to SSDOM and Components and other.",
                "url": "https://mojahid-0-youness.github.io/probo/",
            },
            {
                "title": "User Guide",
                "desc": "Build your first python UI from scratch.",
                "url": "https://mojahid-0-youness.github.io/probo/user_guide/",
            },
            {
                "title": "Community",
                "desc": "Join our Discord and help us reach 1000 tests.",
                "url": "https://discord.gg/jnZRbVasgd",
            },
        ]

        return SECTION(
            DIV(
                *[
                    A(
                        H2(l["title"], **documentation_link_heading_style),
                        P(l["desc"], **documentation_link_paragraph_style),
                        href=l["url"],
                        Class="card-link",
                        **documentation_link_style,
                    )
                    for l in links
                ],
                **documentation_container_style,
            ),
            **documentation_section_style,
        )

    def FooterStatus():
        """Shows the engine status and version."""
        return FOOTER(DIV(
            P("Probo UI v1.3.0 — 800+ Tests Passed", **footer_paragraph_status),
            **footer_section,
        ))

    # Initialize our standard base tree
    doc = base_template_tree(overide_body=True)

    # Register our launch animations in the head
    doc.html_doc.find(lambda n:n.element_tag == 'style').content.append(LAUNCH_STYLE)

    # Build the Body structure
    layout = MAIN(
        HeroSection(),
        DocumentationLinks(),
        FooterStatus(),
        **main_section_style,
    )

    # Inject into the document
    doc.html_doc.find(lambda n: n.element_tag == "body").add(layout)

    return doc

