import typer
import sys
import os
from rich.console import Console
from pathlib import Path
from enum import Enum
from importlib.util import spec_from_file_location, module_from_spec
import webbrowser
import code as python_code
import subprocess
from rich.panel import Panel
from rich.syntax import Syntax
from probo.terminal.emmet import emmet
from probo.terminal.app_generator import (
    create_probo_dj_structure,
    create_hacksoft_structure,
)

app = typer.Typer(
    help="PROBO: The declarative rendering engine for Django.", add_completion=False
)
console = Console()
VERSION = "1.2.0"

def load_tcm_registry(path: Path):
    """
    Dynamically loads the 'probo_tcm.py' file from the user's project.
    Returns the 'tcm' object containing the registered components.
    """
    if not path.exists():
        console.print(
            f"[red] Error: Could not find '{path}'. Are you in the project root?[/red]"
        )
        raise typer.Exit(code=1)

    # Add current directory to sys.path so the user's code can import their own modules
    sys.path.append(str(Path.cwd()))

    try:
        spec = spec_from_file_location("probo_tcm", path)
        module = module_from_spec(spec)
        spec.loader.exec_module(module)

        if not hasattr(module, "tcm"):
            console.print(
                f"[red] Error: '{path}' exists but does not export a 'tcm' object.[/red]"
            )
            raise typer.Exit(code=1)
        return module.tcm

    except Exception as e:
        console.print(f"[red] Error loading registry: {e}[/red]")
        raise typer.Exit(code=1)

try:
    import readline
    import rlcompleter
    if 'libedit' in readline.__doc__:
        readline.parse_and_bind("bind ^I rl_complete")
    else:
        readline.parse_and_bind("tab: complete")
except ImportError:
    # On some systems (like Windows without pyreadline), this might fail
    pass

class ProboConsole(python_code.InteractiveConsole):
    """
    A custom Python console that intercepts input to allow 'naked' 
    Emmet shorthand without quotes.
    """
    def push(self, line):
        # 1. Look for Emmet markers: starts with a tag, contains #, ., -c, or -s
        # We check if it's NOT already quoted and looks like shorthand
        is_shorthand = any(marker in line for marker in [' -c ', ' -s ', ' #', ' .'])
        
        # Also check if it starts with a common tag followed by a space
        common_tags = ['div', 'p', 'span', 'section', 'h1', 'h2', 'h3', 'a', 'ul', 'li']
        starts_with_tag = any(line.strip().startswith(tag + " ") for tag in common_tags)

        if (is_shorthand or starts_with_tag) and not (line.strip().startswith('"') or line.strip().startswith("'")):
            # Auto-wrap the line in quotes so Python treats it as a string
            line = f'"{line.strip()}"'
        
        # 2. Pass the (potentially modified) line to the real Python interpreter
        return super().push(line)

def save_to_dist(value, filename="index.html"):
    """
    Saves the rendered HTML of a component or a string to the dist/ directory.
    """
    dist_path = "dist"
    if not os.path.exists(dist_path):
        os.makedirs(dist_path)
    
    file_path = os.path.join(dist_path, filename)
    
    # Handle renderable objects or strings
    html_content = value.render() if hasattr(value, "render") else str(value)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    console.print(f"[bold green]✓[/bold green] Exported to [cyan]{file_path}[/cyan]")

# --- ARCHITECTURE DEFINITIONS ---

class DjangoStructure(str, Enum):
    BASE = "base"  # Standard Django (MVT)
    HACKSOFT = "hacksoft"  # Domain-Driven (Services/Selectors)
    PROBO_DJ = "probo-dj"  # Enterprise (Split Views/Forms + Root Utils)

# ==============================================================================
#  1. PURE PROBO PROJECT (Standalone)
# ==============================================================================

@app.command("init")
def init(name: str):
    """
    Initializes a new Probo project directory.
    using bottle as server via ProboRouter.
    Best for prototyping, landing pages, or HTMX-only sites.

    Arguments:

    name: The name of the project folder.

    Actions: Creates the standard scaffold including pages/, components/, static/, and the probo_tcm.py registry.
    """
    # project_dir_parent = Path.cwd() / name
    # project_dir = Path.cwd() / project_dir_parent / name
    project_dir = Path.cwd() / name
    if project_dir.exists():
        console.print(f"[red]Error: Directory '{name}' already exists![/red]")
        raise typer.Exit(1)

    project_dir.mkdir(parents=True)

    # 1. The Entry Point
    (project_dir / "main.py").write_text(
        f"""from probo.router import ProboRouter
from probo import div, h1

router = ProboRouter(app_name="{name}")

if __name__ == "__main__":
    print("Building static {name} site...")
    router.load_tcm()
    @router.page("/")
    def home_view(request,response):
        return {{'greeting':div(
            h1("Welcome to {name}"),
        )}}
    router.run(port=8080) # any port is okay :)
""",
        encoding="utf-8",
    )

    # 2. The Registry
    (project_dir / "probo_tcm.py").write_text(
        """from probo.context import TemplateComponentMap
tcm = TemplateComponentMap()
# example usage
# from components.home import HomePageBanner
# tcm.set_component(home=HomePageBanner())
""",
        encoding="utf-8",
    )

    (project_dir / "__init__.py").touch()
    # 3. The Components Layer
    (project_dir / "components").mkdir()
    (project_dir / "components" / "__init__.py").touch()
    (project_dir / "components" / "header.py").touch()

    (project_dir / "pages").mkdir()
    (project_dir / "pages" / "index.py").touch()
    (project_dir / "pages" / "__init__.py").touch()

    # 4. Assets
    (project_dir / "static").mkdir()
    (project_dir / "static" / "assets").mkdir()
    (project_dir / "static" / "assets" / "style.css").write_text(
        """
*::before {
  content: " "; /* Unicode for a non-breaking space */
}""",
        encoding="utf-8",
    )
    (project_dir / "dist").mkdir()  # Output folder

    console.print(f"[green]✨ Pure PROBO Project '{name}' initialized![/green]")
    console.print(f"[dim]Run 'cd {name}' then 'probo shell' to start building static pages.[/dim]")

# ==============================================================================
#  2. DJANGO APP INTEGRATION
# ==============================================================================

@app.command("dj-app")
def startapp(
    name: str,
    structure: DjangoStructure = typer.Option(
        DjangoStructure.BASE,
        "--structure",
        "-s",
        help="Choose architecture: 'base' (Standard), 'hacksoft' (DDD), or 'probo-dj' (Enterprise).",
    ),
):
    """
    Create a Django app with PROBO folders.
    Scaffolds a new application module or a specific feature set within an existing project.
    available flags:
        base: standard django app
        probo-dj: standard django app + probo-ui dependencies
        hacksoft: standard django app + hacksoft archetecture

    Usage: Used to keep your project modular as it scales beyond a single pages/ directory.

    """
    # 1. Run standard Django command
    try:
        subprocess.run([sys.executable, "manage.py", "startapp", name], check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        console.print(
            "[red]Error: Could not run 'manage.py'. Are you in the root of a Django project?[/red]"
        )
        return

    app_dir = Path.cwd() / name
    # 2. Common PROBO Layer (All structures get this)
    components_dir = app_dir / "components"
    components_dir.mkdir(parents=True, exist_ok=True)
    (components_dir / "__init__.py").touch()
    (app_dir / "probo_tcm.py").write_text(""" # utilities for django views and multi-component mapping
from probo.context import TemplateComponentMap
from django.utils.safestring import mark_safe
from django.template import Template, RequestContext

def render_probo(request, *raw_template_strings,**context):
    ''' use this to desplay html string as safe html and use it as django's render '''
    raw_template_string = ''.join([tmplt.render() if hasattr(tmplt,'render') else str(tmplt) for tmplt in raw_template_strings])
    context = RequestContext(request, context)
    template = Template(raw_template_string)

    # 4. Render and Return
    return mark_safe(template.render(context))

tcm = TemplateComponentMap() #mapper of component objects

""")

    # 3. Apply Structure Logic
    if structure == DjangoStructure.HACKSOFT:
        create_hacksoft_structure(app_dir)
        console.print(f"[green]✨ Created App '{name}' (HackSoft Style)[/green]")

    elif structure == DjangoStructure.PROBO_DJ:
        create_probo_dj_structure(app_dir, name)
        console.print(f"[green]✨ Created App '{name}' (PROBO-DJ Enterprise)[/green]")

    else:
        console.print(f"[green]✨ Created App '{name}' (Base Style)[/green]")

    # Visual Confirmation
    console.print("   + components/")
    console.print("   + probo_tcm.py")

@app.command("build:css")
def build_css(registry_path: Path = typer.Option("probo_tcm.py", help="Path to the TCM registry file"),output: Path = typer.Option("static/assets/style.css", help="Output path for the CSS file"),):
    """
    The JIT (Just-In-Time) styling engine. It scans your TCM registry to find all utilized Bootstrap utility classes and Probo-specific styles, merging them into a single optimized CSS file.

    Options:

    --registry-path: Path to your probo_tcm.py (Default: probo_tcm.py).

    --output: The destination for the generated CSS (Default: static/css/style.css)
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
            if hasattr(comp, "elements"):
                for el in comp.elements:
                    el.d_data_key = None  # Force static fallback

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

    console.print(
        "[bold green]CSS Exported ✅✅✅ [/bold green]",
    )
    console.print(
        f"[bold green]✅ Successfully wrote {len(seen_signatures)} unique styles to {output}[/bold green]",
    )

@app.command("build:html")
def build_html(registry_path: Path = typer.Option("probo_tcm.py", help="Path to the TCM registry file"), output_dir: Path = typer.Option("dist", help="Directory to save HTML files"),):
    """
   The Static Site Generation (SSG) command. It iterates through every route defined in your TCM and renders the components into standalone HTML files.

    Options:

    --registry-path: Path to your probo_tcm.py.

    --output-dir: The directory where HTML files will be saved (Default: dist).

    Outcome: A ready-to-deploy static version of your site in the /dist folder.
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
    <title>{name} - PROBO Static Build</title>
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
            console.print(
                f"⚠️  Failed to render {name}: {e}",
            )

    console.print(
        f"[bold green]✅ Generated {count} HTML files.[/bold green]",
    )

@app.command("preview")
def preview_component(component_name: str, registry_path: Path = typer.Option("probo_tcm.py", help="Path to the TCM registry"),):
    """
    Instantly previews a specific component in the browser without needing to navigate through the whole app.

    Arguments:

    component_name: The key or class name of the component in the TCM.

    Options:

    --registry-path: Path to the TCM registry.
    """
    # 1. Load Registry
    tcm = load_tcm_registry(registry_path)

    if component_name not in tcm.url_name_comp:
        console.print(
            f"Error: Component '{component_name}' not found in registry.",
        )
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

        fd, path = tempfile.mkstemp(suffix=".html", prefix=f"probo_{component_name}_")

        with os.fdopen(fd, "w") as tmp:
            tmp.write(full_page)

        # 5. Open Browser (The Logic from your 'brow_a_file')
        file_url = f"file:///{path}"
        console.print(
            f"[blue]👀 Opening preview for {component_name}...[/blue]...",
        )
        webbrowser.open_new_tab(file_url)

    except Exception as e:
        console.print(
            f"Error rendering {component_name}: {e}",
        )

@app.command("shell")
def shell():
    """
    Launches the Probo Interactive REPL. This is a powerful environment for testing component logic.

    Features:

    Emmet Shorthand: Type "naked" commands like div .p-4 -c Hello to see instant HTML results.

    Rich Styling: Beautifully syntax-highlighted HTML output.

    Exporting: Use save(_) to dump your last rendered component into dist/index.html.

    Arrow Keys: Fully supported command history and navigation.
    """
    user_ns = {
        "save": save_to_dist,
        "console": console
    }
    exec("from probo import *", user_ns)
    state = {
        "allow_emmet": True,
        "last_rendered": []
    }
    def displayhook(value):

        if value == 'allow_emmet':
            console.print("""[yellow]•Shorthand enabled:[/yellow] Use [bold magenta]'div #id .class -c content' <==> <div id="id" class="class">content</div>[/bold magenta]""")
            state["allow_emmet"]=True
            return
        if value is None:
            return
        if state["allow_emmet"]:
            value = emmet(value)
        if hasattr(value, "render"):
            html_str = value.render()

            syntax = Syntax(html_str, "html", theme="monokai", line_numbers=False)
            console.print(syntax)

        elif isinstance(value, str) and value.strip().startswith("<"):
            syntax = Syntax(value, "html", theme="monokai")
            console.print(syntax)

        else:
            console.print(value)
        state['last_rendered'].append(value)
        user_ns['_'] = ''.join(state['last_rendered'])
    sys.displayhook = displayhook
    emmet_banner = """\n[yellow]• Shorthand enabled:[/yellow] Use [bold magenta]'div #id .class -c content' <==> <div id="id" class="class">content</div>[/bold magenta]\n type ""allow_emmet" """if state["allow_emmet"] else ''
    banner_text = f"""
    [italic][bold green]PROBO Interactive Shell v1.0[/bold green]
    [yellow]• Standard:[/yellow]  div('Hello', id='main')
    [yellow]• Logic:[/yellow]     loop(5, hr()){emmet_banner}
    [yellow]• Type[/yellow] [bold cyan]save(_)[/bold cyan] to export result to dist/index.html
    [yellow]• Type[/yellow] [red]exit()[/red] to quit.[/italic]
"""
   
    console.print(Panel(banner_text, title="PROBO Console", expand=False))

    console.print(f"[bold blue]Context:[/bold blue] {os.getcwd()}")
    probo_shell = ProboConsole(locals=user_ns)
    
    try:
        probo_shell.interact(banner="",)
    except SystemExit:
        pass

@app.command("version")
def version():
    """Show the current version."""
    # This replaces your 'show_version' method
    console.print(
        f"[bold cyan]Mastodon UI (probo)[/bold cyan] version [yellow]{VERSION}[/yellow]"
    )

@app.command("echo")
def echo(text: str):
    """Print arguments to the console (Debug tool)."""
    # This replaces your 'echo' method
    console.print(f"[italic blue]Echo:[/italic blue] {text}")

def main():
    app()
