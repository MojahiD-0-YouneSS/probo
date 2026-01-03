# Contributing to Probo UI

Thank you for investing your time in contributing to our project!

## 1. Getting Started

1. **Fork** the repository on GitHub.
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/MojahiD-0-YouneSS/probo.git
   ```
3. **Set up a virtual environment and install dependencies**
    cd probo
    python -m venv venv
    source venv/bin/activate
    pip install -e .

4. **Making Changes**
    Create a new branch for your feature: ```git checkout -b my-new-feature.```
    Write your code.
    Ensure you follow our naming conventions:
    **Coding Standards & Style Guide**
        We strictly follow specific naming conventions to keep the library consistent. Please ensure your code adheres to these rules before submitting a PR.

    **Naming Conventions**
    * **Classes:** Use `CamelCase` (PascalCase).
        * *Correct:* `ProboButton`, `ViewRegistry`
        * *Incorrect:* `proboButton`, `view_registry`
        
    * **Functions & Variables:** Use `snake_case`.
        * *Correct:* `get_view_config()`, `user_id`
        * *Incorrect:* `getViewConfig()`, `UserId`

    * **Internal/Scoped Methods:**: Any function or method intended for internal use only (not part of the public API) must start with a single underscore `_`.
        * *Correct:* `def _resolve_url_name(self):`
        * *Incorrect:* `def resolve_url_name(self):` (If it is not meant for the user)

    * **Linting** : We recommend using `flake8` or `black` to check your code style before pushing.
5. **Submitting a Pull Request**
    Push your branch to GitHub.
    Open a Pull Request against the main branch.
    Describe your changes and link to any relevant issues.

💬 Community & Support Need help? Have a question that isn't a bug? Join our <a href='https://discord.gg/jnZRbVasgd'>Discord</a> Server to chat with other probo-ui developers.