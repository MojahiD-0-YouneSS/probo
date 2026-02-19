import sys
from pathlib import Path

# 1. Define source and output paths
src_root = Path("src")
docs_root = Path("docs/reference") # We will write real files here

# 2. Loop through every Python file
for path in src_root.rglob("*.py"):
    
    if path.name == "__init__.py":
        continue

    # Calculate paths
    relative_path = path.relative_to(src_root)
    doc_path = docs_root / relative_path.with_suffix(".md")
    
    # Calculate Python import identifier (e.g., probo.components.button)
    # We strip "src" from the path logic here if your package is just "probo" inside src
    ident = ".".join(relative_path.with_suffix("").parts)

    # 3. SAFETY CHECK: Only create the file if it DOES NOT exist.
    #    This ensures we never overwrite your manual edits.
    if not doc_path.exists():
        
        # Create directories if needed
        doc_path.parent.mkdir(parents=True, exist_ok=True)

        with open(doc_path, "w", encoding="utf-8") as f:
            f.write(f"# {path.stem}\n\n")
            # This is the "Magic Line" that pulls live docs from Python
            f.write(f"::: {ident}\n")
            
        print(f"Created new doc stub: {doc_path}")
