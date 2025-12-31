import pytest
from unittest.mock import patch, mock_open

# Check if bs4 is available, otherwise skip these tests


from src.probo.xml.xml import HtmlToXmlConverter  # Assuming you save your snippet here


class TestHtmlToXmlConverter:
    def test_templating_render(self):
        """1. Test {{ variable }} substitution logic."""
        html = '<div id="{{ id_val }}">{{ content }}</div>'
        converter = HtmlToXmlConverter(html)

        # Chain methods
        converter.with_data({"id_val": "main", "content": "Hello World"}).render()

        # We access the internal html string to verify pre-xml conversion state
        assert '<div id="main">Hello World</div>' in converter._html_string

    def test_basic_conversion_structure(self):
        """2. Test HTML -> XML structure conversion."""
        html = "<span>Text</span>"
        converter = HtmlToXmlConverter(html)

        xml = converter.to_xml()

        # Your class wraps everything in a <root> element
        assert "<root>" in xml
        assert "<span>Text</span>" in xml
        assert "</root>" in xml

    def test_attribute_list_handling(self):
        """3. Test handling of list attributes (like class)."""
        # BeautifulSoup parses class="a b" as ['a', 'b']
        html = '<div class="btn btn-primary"></div>'
        converter = HtmlToXmlConverter(html)

        xml = converter.to_xml()

        # XML converter should join them back to string
        assert 'class="btn btn-primary"' in xml

    def test_nested_structure(self):
        """4. Test recursive nesting."""
        html = "<ul><li>A</li><li>B</li></ul>"
        converter = HtmlToXmlConverter(html)
        xml = converter.to_xml()

        assert "<root><ul><li>A</li><li>B</li></ul></root>" in xml.replace(
            "\n", ""
        ).replace(" ", "")

    def test_pretty_print(self):
        """5. Test pretty print indentation."""
        html = "<div><p>Inner</p></div>"
        converter = HtmlToXmlConverter(html)

        xml = converter.to_xml(pretty_print=True)

        # Check for newlines and indentation
        assert "\n" in xml
        assert "  <div" in xml or "\t<div" in xml

    def test_fragment_parsing(self):
        """6. Test parsing fragments without body tags."""
        html = "Just text and <b>bold</b>"
        converter = HtmlToXmlConverter(html)
        xml = converter.to_xml()

        # Should handle text nodes correctly
        assert "Just text and" in xml
        assert "<b>bold</b>" in xml

    def test_error_handling_empty_load(self):
        """7. Test error when converting empty string."""
        converter = HtmlToXmlConverter("")

        with pytest.raises(ValueError) as exc:
            converter.to_xml()

        assert "No HTML string loaded" in str(exc.value)

    def test_fluent_api_chaining(self):
        """8. Test the chaining capabilities (Fluent Interface)."""
        converter = HtmlToXmlConverter()

        # Should not raise error and return self at each step
        res = converter.load_html("<div></div>").with_data({}).render()

        assert isinstance(res, HtmlToXmlConverter)
        assert res._html_string == "<div></div>"

    def test_validate_xml_placeholder(self):
        """9. Test the simple validation logic."""
        converter = HtmlToXmlConverter("<div></div>")

        # Before generation
        assert converter.validate_xml() is False

        # After generation
        converter.to_xml()
        assert converter.validate_xml() is True

    def test_save_xml_file(self):
        """10. Test file saving mechanism."""
        html = "<data>123</data>"
        converter = HtmlToXmlConverter(html)

        # Mock the open function to avoid writing to disk
        m = mock_open()
        with patch("builtins.open", m):
            converter.save_xml("output.xml")

        # Verify write was called
        m.assert_called_with("output.xml", "w", encoding="utf-8")
        handle = m()
        # Verify content was written (checking start of XML)
        handle.write.assert_any_call(converter.to_xml())
