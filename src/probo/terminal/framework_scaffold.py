import typer
import os
from pathlib import Path
from rich.console import Console

console = Console()

def create_common_files(project_dir: Path, framework: str):
    """Creates common boilerplate files like README and requirements."""
    readme_content = f"# {project_dir.name}\n\nBuilt with Probo and {framework}.\n"
    reqs_content = f"probo\n{framework.lower()}\n"
    
    if framework.lower() == "fastapi":
        reqs_content += "uvicorn\n"
    
    (project_dir / "README.md").write_text(readme_content, encoding="utf-8")
    (project_dir / "requirements.txt").write_text(reqs_content, encoding="utf-8")

def create_ui_boilerplate(ui_dir: Path, include_base: bool = True):
    """Creates the standard ui/ folder with basic Probo components."""
    components_dir = ui_dir / "components"
    components_dir.mkdir(parents=True, exist_ok=True)
    (components_dir / "__init__.py").touch()
    
    (components_dir / "navigation.py").write_text('''from probo import DIV, A, NAV

def navbar():
    return NAV(
        DIV(
            A("Home", href="/"),
            A("About", href="/about"),
            Class="nav-links"
        ),
        Class="navbar"
    )
''', encoding="utf-8")

    if include_base:
        (ui_dir / "__init__.py").touch()
        (ui_dir / "base.py").write_text('''from probo.templates import base_template_tree
from .components.navigation import navbar
from probo import DIV

def get_base_template():
    base = base_template_tree(override_body=True)
    body = base.html_doc.find(lambda n: n.tag == 'BODY')
    if body:
        body.add(navbar())
        body.add(DIV(id="main-content"))
    return base
''', encoding="utf-8")

def scaffold_fastapi(
    name: str,
    structure: str = typer.Option("standard", help="'standard' or 'advanced'"),
):
    """Scaffold a FastAPI project with Probo integration."""
    project_dir = Path.cwd() / name
    project_dir.mkdir(parents=True, exist_ok=True)
    
    app_dir = project_dir / "app"
    app_dir.mkdir(exist_ok=True)
    (app_dir / "__init__.py").touch()
    
    ui_dir = app_dir / "ui"
    ui_dir.mkdir(exist_ok=True)
    
    if structure == "standard":
        (app_dir / "config.py").touch()
        (app_dir / "main.py").write_text('''from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.ui.base import get_base_template
from probo import DIV, H1, P

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    template = get_base_template()
    content = DIV(H1("Welcome to FastAPI + Probo"), P("Hello World"))
    
    # Simple manual mounting for now, or using custom TCM
    main = template.html_doc.find(lambda n: getattr(n, 'id', None) == "main-content")
    if main:
        main.add(content)
        
    return template.render()
''', encoding="utf-8")
        create_ui_boilerplate(ui_dir, include_base=True)
        
    elif structure == "advanced":
        (app_dir / "dependencies.py").touch()
        
        routers_dir = app_dir / "routers"
        routers_dir.mkdir(exist_ok=True)
        (routers_dir / "__init__.py").touch()
        (routers_dir / "items.py").touch()
        (routers_dir / "users.py").touch()
        
        internal_dir = app_dir / "internal"
        internal_dir.mkdir(exist_ok=True)
        (internal_dir / "__init__.py").touch()
        (internal_dir / "admin.py").touch()
        
        (app_dir / "main.py").write_text('''from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.ui.base import get_base_template
from probo import DIV, H1

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    template = get_base_template()
    content = DIV(H1("FastAPI Advanced + Probo"))
    
    main = template.html_doc.find(lambda n: getattr(n, 'id', None) == "main-content")
    if main:
        main.add(content)
        
    return template.render()
''', encoding="utf-8")
        create_ui_boilerplate(ui_dir, include_base=True)
    
    create_common_files(project_dir, "FastAPI")
    console.print(f"[green] <=> Created FastAPI App '{name}' ({structure} structure)[/green]")

def scaffold_litestar(name: str):
    """Scaffold a Litestar project with Probo integration."""
    project_dir = Path.cwd() / name
    project_dir.mkdir(parents=True, exist_ok=True)
    
    app_dir = project_dir / "app"
    app_dir.mkdir(exist_ok=True)
    (app_dir / "__init__.py").touch()
    
    ctrl_dir = app_dir / "controllers"
    ctrl_dir.mkdir(exist_ok=True)
    (ctrl_dir / "__init__.py").touch()
    (ctrl_dir / "home.py").write_text('''from litestar import Controller, get
from litestar.enums import MediaType
from app.ui.layout import get_layout
from app.ui.views.index import home_view

class HomeController(Controller):
    path = "/"

    @get(media_type=MediaType.HTML)
    async def index(self) -> str:
        page = get_layout()
        main = page.html_doc.find(lambda n: getattr(n, 'id', None) == "main-content")
        if main:
            main.add(home_view())
        return page.render()
''', encoding="utf-8")
    
    ui_dir = app_dir / "ui"
    ui_dir.mkdir(exist_ok=True)
    (ui_dir / "__init__.py").touch()
    (ui_dir / "layout.py").write_text('''from probo.templates import base_template_tree
from probo import DIV, NAV, A

def get_layout():
    base = base_template_tree(override_body=True)
    body = base.html_doc.find(lambda n: n.tag == 'BODY')
    if body:
        body.add(NAV(A("Home", href="/")))
        body.add(DIV(id="main-content"))
    return base
''', encoding="utf-8")
    
    views_dir = ui_dir / "views"
    views_dir.mkdir(exist_ok=True)
    (views_dir / "__init__.py").touch()
    (views_dir / "index.py").write_text('''from probo import DIV, H1, P

def home_view():
    return DIV(
        H1("Litestar + Probo"),
        P("Welcome to Litestar running Probo UI!")
    )
''', encoding="utf-8")
    
    (app_dir / "main.py").write_text('''from litestar import Litestar
from app.controllers.home import HomeController

app = Litestar(route_handlers=[HomeController])
''', encoding="utf-8")

    create_common_files(project_dir, "Litestar")
    console.print(f"[green] <=> Created Litestar App '{name}'[/green]")

def scaffold_flask(name: str):
    """Scaffold a Flask project with Probo integration."""
    project_dir = Path.cwd() / name
    project_dir.mkdir(parents=True, exist_ok=True)
    
    app_dir = project_dir / "app"
    app_dir.mkdir(exist_ok=True)
    (app_dir / "__init__.py").touch()
    
    (app_dir / "routes.py").write_text('''from flask import Blueprint
from app.ui.base_template import get_base_template
from app.ui.components import hero_component

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    template = get_base_template()
    main = template.html_doc.find(lambda n: getattr(n, 'id', None) == "main-content")
    if main:
        main.add(hero_component())
    return template.render()
''', encoding="utf-8")

    ui_dir = app_dir / "ui"
    ui_dir.mkdir(exist_ok=True)
    (ui_dir / "__init__.py").touch()
    
    (ui_dir / "base_template.py").write_text('''from probo.templates import base_template_tree
from probo import DIV

def get_base_template():
    base = base_template_tree(override_body=True)
    body = base.html_doc.find(lambda n: n.tag == 'BODY')
    if body:
        body.add(DIV(id="main-content"))
    return base
''', encoding="utf-8")

    (ui_dir / "components.py").write_text('''from probo import DIV, H1, P

def hero_component():
    return DIV(
        H1("Flask + Probo"),
        P("This is a Flask app using Probo declarative UI.")
    )
''', encoding="utf-8")

    (project_dir / "config.py").touch()
    (project_dir / "run.py").write_text('''from flask import Flask
from app.routes import main_bp

app = Flask(__name__)
app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(debug=True)
''', encoding="utf-8")

    create_common_files(project_dir, "Flask")
    console.print(f"[green] <=> Created Flask App '{name}'[/green]")

def scaffold_cherrypy(name: str):
    """Scaffold a CherryPy project with Probo integration."""
    project_dir = Path.cwd() / name
    project_dir.mkdir(parents=True, exist_ok=True)
    
    ui_dir = project_dir / "ui"
    ui_dir.mkdir(exist_ok=True)
    (ui_dir / "__init__.py").touch()
    
    (ui_dir / "base.py").write_text('''from probo.templates import base_template_tree
from probo import DIV

def get_base_template():
    base = base_template_tree(override_body=True)
    body = base.html_doc.find(lambda n: n.tag == 'BODY')
    if body:
        body.add(DIV(id="main-content"))
    return base
''', encoding="utf-8")

    (ui_dir / "components.py").write_text('''from probo import DIV, H1, P

def greeting():
    return DIV(H1("CherryPy + Probo"), P("Declarative UI in CherryPy"))
''', encoding="utf-8")

    (project_dir / "app.py").write_text('''import cherrypy
from ui.base import get_base_template
from ui.components import greeting

class Root(object):
    @cherrypy.expose
    def index(self):
        template = get_base_template()
        main = template.html_doc.find(lambda n: getattr(n, 'id', None) == "main-content")
        if main:
            main.add(greeting())
        return template.render()

if __name__ == '__main__':
    cherrypy.quickstart(Root())
''', encoding="utf-8")

    create_common_files(project_dir, "CherryPy")
    console.print(f"[green] <=> Created CherryPy App '{name}'[/green]")
