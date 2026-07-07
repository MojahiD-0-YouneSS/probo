from probo.components.conf import settings
from probo.components.tag_classes.block_tags import DIV

settings.TITLE = "Global Probo Title"
settings.SECTION_I = "Hero Section"

print(f"debug settings id: {id(settings)}")
print(f"debug get('TITLE'): {settings.get('TITLE')}")

test_node = DIV({'TITLE'}, " - ", {'SECTION_I'},data_pipeline=settings)
print(f"Parent: {test_node.parent}")
print(f"TITLE get_data: {test_node.get_data('TITLE')}")

html = test_node.render()
print(f"HTML: {html}")
