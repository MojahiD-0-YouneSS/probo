from src.probo.xml.elements import (
    XMLElement,
    XMLSection,
    XMLDocument,
    XMLComment,
    XMLInstruction,
)

# ==============================================================================
#  GROUP 1: XMLElement (5 Tests)
# ==============================================================================


def test_xml_element_basic():
    """1. Basic tag generation."""
    el = XMLElement("user", id="123")
    assert el.render() == '<user id="123" />'  # Self-closing if empty


def test_xml_element_content():
    """2. Tag with string content."""
    el = XMLElement("name", "Youness")
    assert el.render() == "<name>Youness</name>"


def test_xml_element_nesting():
    """3. Nested elements."""
    child = XMLElement("item", "Data")
    parent = XMLElement("list")
    parent.add(child)

    expected = "<list><item>Data</item></list>"
    assert parent.render() == expected


def test_xml_element_case_sensitivity():
    """4. XML tags are case-sensitive."""
    el = XMLElement("camelCase")
    assert "<camelCase" in el.render()
    assert "</camelCase>" not in el.render()


def test_xml_element_attributes_strict():
    """5. Verify attributes are key="value" (No boolean flags)."""
    el = XMLElement("video", autoplay=True, controls=None)

    rendered = el.render()
    # XML doesn't support 'autoplay', must be 'autoplay="autoplay"' or similar
    # Your implementation handles True -> key="key"
    assert 'autoplay="autoplay"' in rendered
    # None/False should be skipped
    assert "controls" not in rendered


# ==============================================================================
#  GROUP 2: XMLSection & Utilities (5 Tests)
# ==============================================================================


def test_xml_cdata_section():
    """6. CDATA Wrapping."""
    raw_code = "if (x < y && z > 0)"
    cdata = XMLSection(raw_code)

    assert cdata.render() == f"<![CDATA[{raw_code}]]>"


def test_xml_comment():
    """7. Comments."""
    comm = XMLComment("This is metadata")
    assert comm.render() == "<!-- This is metadata -->"


def test_xml_instruction_simple():
    """8. Processing Instructions (PI)."""
    pi = XMLInstruction("php", "echo 'hi';")
    assert pi.render() == "<?php echo 'hi';?>"


def test_xml_instruction_stylesheet():
    """9. XSL Stylesheet instruction."""
    pi = XMLInstruction("xml-stylesheet", 'type="text/xsl" href="style.xsl"')
    assert pi.render() == '<?xml-stylesheet type="text/xsl" href="style.xsl"?>'


def test_xml_element_add_fluent():
    """10. Fluent API chaining."""
    el = XMLElement("root").add("Text").add(XMLElement("child"))
    assert "<root>Text<child /></root>" == el.render()


# ==============================================================================
#  GROUP 3: XMLDocument (5 Tests)
# ==============================================================================


def test_xml_document_default_declaration():
    """11. Standard declaration."""
    doc = XMLDocument(root=XMLElement("data"))
    xml = doc.render()

    assert '<?xml version="1.0" encoding="UTF-8"?>' in xml
    assert "<data />" in xml


def test_xml_document_custom_declaration():
    """12. Custom version/encoding."""
    doc = XMLDocument(root=XMLElement("svg"), version="1.1", encoding="ISO-8859-1")
    xml = doc.render()

    assert 'version="1.1"' in xml
    assert 'encoding="ISO-8859-1"' in xml


def test_xml_document_standalone():
    """13. Standalone declaration."""
    doc = XMLDocument("root", standalone="yes")
    xml = doc.render()

    assert 'standalone="yes"' in xml


def test_xml_document_full_structure():
    """14. Declaration + Instruction + Root."""
    root = XMLElement("feed")
    doc = XMLDocument(root=root)
    doc.add_instruction("xml-stylesheet", 'href="rss.css"')

    xml = doc.render()

    # Order Check
    decl_pos = xml.find("<?xml")
    instr_pos = xml.find("<?xml-stylesheet")
    root_pos = xml.find("<feed")

    assert decl_pos < instr_pos < root_pos


def test_xml_document_init_root_config():
    """15. Initialize root element via document constructor args."""
    # Assuming __init__ passes kwargs to root element creation if tag provided
    # or takes an XMLElement instance directly.
    # Based on your code: __init__(self, root: Optional[XMLElement]...)

    root_el = XMLElement("rss", version="2.0")
    doc = XMLDocument(root=root_el)

    assert '<rss version="2.0" />' in doc.render()
