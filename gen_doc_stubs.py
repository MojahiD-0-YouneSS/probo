import mkdocs_gen_files
from pathlib import Path

src_root = Path("src")

for path in src_root.rglob("*.py"):
    if path.name == "__init__.py":
        continue

    # Path relative to src (e.g. "probo/utility.py")
    relative_path = path.relative_to(src_root)
    
    # Doc file location (e.g. "reference/probo/utility.md")
    doc_path = Path("reference", relative_path).with_suffix(".md")
    
    # Python import path (e.g. "probo.utility" instead of "src.probo.utility")
    # ✅ FIX: We use relative_path here so "src" is NOT included in the dot notation
    ident = ".".join(relative_path.with_suffix("").parts)

    with mkdocs_gen_files.open(doc_path, "w") as f:
        f.write(f"# {path.stem}\n\n")
        f.write(f"::: {ident}")

    mkdocs_gen_files.set_edit_path(doc_path, path)
