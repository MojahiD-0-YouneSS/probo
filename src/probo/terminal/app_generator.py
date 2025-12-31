# from django.core.management import call_command
# from django.utils.text import slugify
# List of app names to generate
from pathlib import Path


def create_hacksoft_structure(app_dir: Path):
    """Services (Write) + Selectors (Read)."""
    for folder in ["services", "selectors"]:
        d = app_dir / folder
        d.mkdir(parents=True, exist_ok=True)
        (d / "__init__.py").touch()
        (d / f"{folder}.py").touch()


def create_mui_dj_structure(app_dir: Path, app_name: str):
    """The Full Enterprise Stack."""
    # 1. Deep Layer Separation
    structure = {
        "services": ["__init__.py", f"{app_name}_service.py", "systems/"],
        "selectors": ["__init__.py", "selectors.py"],
        # Split Views & Forms into Admin/Client
        "forms": ["__init__.py", "admin_forms/", "client_forms/"],
        "views": ["__init__.py", "admin_views/", "client_views/"],
        "urls": ["__init__.py", "admin_urls.py", "client_urls.py"],
        "exceptions": ["__init__.py", "service_exception.py"],
    }

    for folder, files in structure.items():
        folder_path = app_dir / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        for f in files:
            if f.endswith("/"):
                (folder_path / f).mkdir(parents=True, exist_ok=True)
            else:
                (folder_path / f).touch()

    # 2. Root Utilities
    for f in ["signals.py", "dependencies.py", "tasks.py"]:
        (app_dir / f).touch()


"""
# Add-on files to be created after generating the app
add_on_files = [
    'dependencies.py',
    'tasks.py',
    'helperfunctions.py',
    'utilities.py',
    'signals.py', 'root_urls.py',

]
add_on_folder = {'services':['__init__.py','creators.py','creator_dependency.py','app_service.py', 'systems/'],
                 'selectors': ['__init__.py','selectors.py','selector_dependency.py',],
                 'forms':['__init__.py','admin_forms/model_form.py','admin_forms/custom_form.py','client_forms/model_form.py','client_forms/custom_form.py',], 
                 'exceptions':['__init__.py','service_exception.py', 'selector_exception.py','system_exception.py',],
                 'views':['__init__.py','admin_views/crud_views.py','admin_views/custom_views.py','client_views/crud_views.py','client_views/custom_views.py',], 
                 'urls':['__init__.py','admin_urls.py', 'client_urls.py',], 
                 'tasks':['__init__.py',],
                 'middleware':['__init__.py',],}

current_dir =  os.path.join(os.getcwd(), 'enterprise_suite_package/app')

def create_add_on_files(app_name):
    # List of additional files to create for each app
    app_dir = os.path.join(current_dir,app_name)
    core_file = ['base_model.py', 
                 'base_form.py', 
                 'base_dependency.py', 
                 'base_selector.py', 
                 'base_service.py', 
                 'base_exception.py', 
                 'regestry.py', 
                 ]
    # Create each add-on file
    if app_name == 'core' :
        for file in core_file:
            file_path = os.path.join(app_dir, file)
            if not os.path.exists(file):  # Check if the file already exists
                with open(file_path, 'w') as f:
                    f.write(f"# {app_name} {file}\n")
                print(f"Created {file} !!!")
            else:
                print(f"{file} already exists in {app_name}, skipping.")
    # Create the add_on folder and files
    for folder, contents in add_on_folder.items():
        folder_path = os.path.join(app_dir, folder)
        os.makedirs(folder_path, exist_ok=True)
        print(f"Created folder: {folder_path}")
        for item in contents:
            if item == 'app_service.py':
                item = f'{app_name}_service.py'
            item_path = os.path.join(folder_path, item)
            if item.endswith('/'):
                # Create subfolder if item is a directory
                os.makedirs(item_path, exist_ok=True) 
                print(f"Created folder: {folder_path}")  
            else:
                # Ensure directory for nested files exists
                os.makedirs(os.path.dirname(item_path), exist_ok=True)
                # Create empty file
                with open(item_path, 'w') as f:
                    pass
                
                print(f"Created {item} in {folder}")        
    for add_on in add_on_files:
        file_path = os.path.join(app_dir, add_on)
        if not os.path.exists(file_path):  # Check if the file already exists
            with open(file_path, 'w') as f:
                f.write(f"# {app_name} {add_on}\n")
            print(f"Created {file_path}")
        else:
            print(f"{add_on} already exists in {app_name}, skipping.")

# Function to create a Django app using `startapp` and add custom files
def create_django_app(app_name):
    # Use Django's startapp command to generate the basic app structure
    try:
        print(f"Creating Django app: {app_name}")
        app_name = slugify(app_name)
        # Get the current working directory
        target_dir = os.path.join(current_dir, app_name)

        if os.path.exists(target_dir):
            print(f"App folder '{target_dir}' already exists. Django won't overwrite it.")
        else:
            # Make sure base dir exists
            os.makedirs(current_dir, exist_ok=True)

            # Save current directory
            prev_cwd = os.getcwd()

            # Change to the parent directory
            os.chdir(current_dir)

            # Call startapp with only the app name
            call_command('startapp', app_name)

            # Change back to original working directory
            os.chdir(prev_cwd)
            create_add_on_files(app_name)


            print(f"App '{app_name}' created at '{target_dir}'")

        # After app is created, add the custom files

    except Exception as e:
        print(f"Error creating app {app_name}: {str(e)}")

# Loop through the app names and generate the apps
def generate_django_apps(structure_type='hack-soft'):
    for app_name in app_names:
        create_django_app(app_name)

"""
