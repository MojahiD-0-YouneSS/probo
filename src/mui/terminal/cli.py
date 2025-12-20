import typer
import sys
import os
from rich.console import Console
from pathlib import Path
from enum import Enum
from importlib.util import spec_from_file_location, module_from_spec
import webbrowser
import code as python_code
import sys
import subprocess
from rich.panel import Panel
from rich.syntax import Syntax
from rich.traceback import install
from mui.terminal.app_generator import (create_mui_dj_structure,create_hacksoft_structure)
app = typer.Typer(
    help="MUI: The declarative rendering engine for Django.",
    add_completion=False
)
console = Console()
VERSION = "1.0.0"

def load_tcm_registry(path: Path):
    """
    Dynamically loads the 'mui_tcm.py' file from the user's project.
    Returns the 'tcm' object containing the registered components.
    """
    if not path.exists():
        console.print(f"[red] Error: Could not find '{path}'. Are you in the project root?[/red]")
        raise typer.Exit(code=1)

    # Add current directory to sys.path so the user's code can import their own modules
    sys.path.append(str(Path.cwd()))

    try:
        spec = spec_from_file_location("mui_tcm", path)
        module = module_from_spec(spec)
        spec.loader.exec_module(module)
        
        if not hasattr(module, 'tcm'):
            console.print(f"[red] Error: '{path}' exists but does not export a 'tcm' object.[/red]")
            raise typer.Exit(code=1)
            
        return module.tcm
    except Exception as e:
        console.print(f"[red] Error loading registry: {e}[/red]")
        raise typer.Exit(code=1)


# --- ARCHITECTURE DEFINITIONS ---

class DjangoStructure(str, Enum):
    BASE = "base"           # Standard Django (MVT)
    HACKSOFT = "hacksoft"   # Domain-Driven (Services/Selectors)
    MUI_DJ = "mui-dj"       # Enterprise (Split Views/Forms + Root Utils)

# ==============================================================================
#  1. PURE MUI PROJECT (Standalone)
# ==============================================================================

@app.command("init")
def init(name: str):
    """
    Scaffold a pure 'MUI Project' (Standalone / Static Site).
    Best for prototyping, landing pages, or HTMX-only sites.
    """
    project_dir = Path.cwd() / name
    if project_dir.exists():
        console.print(f"[red]Error: Directory '{name}' already exists![/red]")
        raise typer.Exit(1)

    project_dir.mkdir(parents=True)
    
    # 1. The Entry Point
    (project_dir / "main.py").write_text("""
from mui.cli import build_html, build_css
if __name__ == "__main__":
    print("Building static site...")
    # Add build logic here
""", encoding="utf-8")

    # 2. The Registry
    (project_dir / "mui_tcm.py").write_text("""
from mui import TemplateComponentMap
tcm = TemplateComponentMap()
# from components.pages import HomePage
# tcm.register(home=HomePage)
""", encoding="utf-8")

    # 3. The Components Layer
    (project_dir / "components").mkdir()
    (project_dir / "components" / "__init__.py").touch()
    (project_dir / "components" / "pages.py").touch()
    
    # 4. Assets
    (project_dir / "assets").mkdir()
    (project_dir / "dist").mkdir() # Output folder

    console.print(f"[green]✨ Pure MUI Project '{name}' initialized![/green]")
    console.print(f"[dim]Run 'cd {name}' then 'mui shell' to start building.[/dim]")

# ==============================================================================
#  2. DJANGO APP INTEGRATION
# ==============================================================================

@app.command("dj-app")
def startapp( name: str, structure: DjangoStructure = typer.Option( DjangoStructure.BASE, "--structure", "-s",  help="Choose architecture: 'base' (Standard), 'hacksoft' (DDD), or 'mui-dj' (Enterprise).")):
    """
    Create a Django app with MUI scaffolding.
    """
    # 1. Run standard Django command
    try:
        subprocess.run([sys.executable, "manage.py", "startapp", name], check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        console.print("[red]Error: Could not run 'manage.py'. Are you in the root of a Django project?[/red]")
        return

    app_dir = Path.cwd() / name
    # 2. Common MUI Layer (All structures get this)
    components_dir = app_dir / "components"
    components_dir.mkdir(parents=True, exist_ok=True)
    (components_dir / "__init__.py").touch()
    (app_dir / "mui_tcm.py").write_text("""
from mui import TemplateComponentMap

from django.http import HttpResponse
from django.template import Template, RequestContext
def render_mui(request, *raw_template_strings,**context):
    ''' use this to desplay html string as safe html and use it as django's render '''
    raw_template_string = ''.join(raw_template_strings)
    context = RequestContext(request, context)
    template = Template(raw_template_string)

    # 4. Render and Return
    return HttpResponse(template.render(context))

tcm = TemplateComponentMap() #mapper of component objects
""")

    # 3. Apply Structure Logic
    if structure == DjangoStructure.HACKSOFT:
        create_hacksoft_structure(app_dir)
        console.print(f"[green]✨ Created App '{name}' (HackSoft Style)[/green]")
        
    elif structure == DjangoStructure.MUI_DJ:
        create_mui_dj_structure(app_dir, name)
        console.print(f"[green]✨ Created App '{name}' (MUI-DJ Enterprise)[/green]")
        
    else:
        console.print(f"[green]✨ Created App '{name}' (Base Style)[/green]")

    # Visual Confirmation
    console.print(f"   + components/")
    console.print(f"   + mui_tcm.py")

@app.command("build:css")
def build_css( registry_path: Path = typer.Option("mui_tcm.py", help="Path to the TCM registry file"), output: Path = typer.Option("static/css/style.css", help="Output path for the CSS file")):
    """
    Scans all registered components, triggers JIT compilation, 
    deduplicates styles, and exports a single CSS bundle.
    """
    tcm = load_tcm_registry(registry_path)
    
    seen_signatures = set()
    final_css_blocks = []
    
    typer.echo(f"🎨 Scanning {len(tcm.url_name_comp)} components for JIT CSS...")

    for name, ComponentClass in tcm.url_name_comp.items():
        try:
            # 1. Mock Render (Force Design Mode / Static Defaults)
            # We assume the component can render with default s_data
            comp = ComponentClass()
            # If you implemented the 'strict_dynamic' logic, ensure defaults are used
            if hasattr(comp, 'elements'):
                for el in comp.elements:
                    el.d_data_key = None # Force static fallback
            
            _, css_output = comp.render()

            if not css_output:
                continue

            # 2. Deduplicate
            css_hash = hash(css_output)
            if css_hash not in seen_signatures:
                seen_signatures.add(css_hash)
                final_css_blocks.append(f"/* --- Component: {name} --- */")
                final_css_blocks.append(css_output)

        except Exception as e:
            console.print(f"[yellow]⚠️  Skipping {name}: {e}[/yellow]")

    # 3. Write
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(final_css_blocks), encoding="utf-8")

    console.print(f"[bold green]CSS Exported ✅✅✅ [/bold green]",)
    console.print(f"[bold green]✅ Successfully wrote {len(seen_signatures)} unique styles to {output}[/bold green]",)

@app.command("build:html")
def build_html( registry_path: Path = typer.Option("mui_tcm.py", help="Path to the TCM registry file"), output_dir: Path = typer.Option("dist", help="Directory to save HTML files")):
    """
    Renders all registered components as static HTML files.
    Useful for prototyping or static site generation.
    """
    tcm = load_tcm_registry(registry_path)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    typer.echo(f"🏗️  Rendering components to '{output_dir}/'...")

    count = 0
    for name, ComponentClass in tcm.url_name_comp.items():
        try:
            # 1. Render
            comp = ComponentClass()
            html_output, css_output = comp.render()

            # 2. Construct Full Page (Inject CSS for standalone viewing)
            full_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - MUI Static Build</title>
    <style>
        {css_output}
    </style>
</head>
<body>
    {html_output}
</body>
</html>"""

            # 3. Save
            file_path = output_dir / f"{name}.html"
            file_path.write_text(full_page, encoding="utf-8")
            count += 1
            typer.echo(f"   📄 Generated: {file_path}")

        except Exception as e:
            console.print(f"⚠️  Failed to render {name}: {e}",)

    console.print(f"[bold green]✅ Generated {count} HTML files.[/bold green]",)

@app.command("preview")
def preview_component( component_name: str, registry_path: Path = typer.Option("mui_tcm.py", help="Path to the TCM registry"),
):
    """
    Renders a specific component, saves it to a temporary file, 
    and opens it in your default browser immediately.
    """
    # 1. Load Registry
    tcm = load_tcm_registry(registry_path)
    
    if component_name not in tcm.url_name_comp:
        console.print(f"Error: Component '{component_name}' not found in registry.",)
        return

    try:
        # 2. Render
        ComponentClass = tcm.url_name_comp[component_name]
        comp = ComponentClass()
        html_output, css_output = comp.render()

        # 3. Wrap in HTML Shell
        full_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Preview: {component_name}</title>
    <style>
        body {{ font-family: system-ui; padding: 2rem; }}
        /* Component Styles */
        {css_output}
    </style>
</head>
<body>
    <div style="border: 1px dashed #ccc; padding: 1rem;">
        {html_output}
    </div>
    <div style="margin-top: 1rem; color: #666; font-size: 0.8rem;">
        Rendering: <strong>{component_name}</strong>
    </div>
</body>
</html>"""

        # 4. Save to Temp File (The Logic from your 'build_logic')
        import tempfile
        fd, path = tempfile.mkstemp(suffix=".html", prefix=f"mui_{component_name}_")
        
        with os.fdopen(fd, 'w') as tmp:
            tmp.write(full_page)
            
        # 5. Open Browser (The Logic from your 'brow_a_file')
        file_url = f"file:///{path}"
        console.print(f"[blue]👀 Opening preview for {component_name}...[/blue]...",)
        webbrowser.open_new_tab(file_url)

    except Exception as e:
        console.print(f"Error rendering {component_name}: {e}",)

@app.command("shell")
def shell():
    """
    Starts an interactive Python shell with MUI pre-loaded and Rich styling.
    """
    user_ns = {}
    exec("from mui import *", user_ns)
    def displayhook(value):
        if value is None:
            return
        
        if hasattr(value, 'render'):
            html_str = value.render()

            syntax = Syntax(html_str, "html", theme="monokai", line_numbers=False)
            console.print(syntax)
            
        elif isinstance(value, str) and value.strip().startswith("<"):
            syntax = Syntax(value, "html", theme="monokai")
            console.print(syntax)
            
        else:
            console.print(value)

    sys.displayhook = displayhook

    banner_text = """
    [bold green]MUI Interactive Shell v1.0[/bold green]
    [yellow]• Standard:[/yellow]  div('Hello', id='main')
    [yellow]• Shorthand:[/yellow] emmet('div #main .container -c Content')
    [yellow]• Logic:[/yellow]     loop(5, hr())
    [italic]Type [red]exit()[/red] to quit.[/italic]"""

    console.print(Panel(banner_text, title="MUI Console", expand=False))

    #user_ns = locals()
    console.print(f"[bold blue]Context:[/bold blue] {os.getcwd()}")
    
    try:
        python_code.interact(banner="", local=user_ns)
    except SystemExit:
        pass

@app.command("version")
def version():
    """Show the current version."""
    # This replaces your 'show_version' method
    console.print(f"[bold cyan]Mastodon UI (mui)[/bold cyan] version [yellow]{VERSION}[/yellow]")

@app.command("echo")
def echo(text: str):
    """Print arguments to the console (Debug tool)."""
    # This replaces your 'echo' method
    console.print(f"[italic blue]Echo:[/italic blue] {text}")

def main():
    app()
