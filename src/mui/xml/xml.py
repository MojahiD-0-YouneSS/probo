import re
from bs4 import BeautifulSoup, NavigableString, Tag
from xml.etree import ElementTree as ET
from xml.dom import minidom # For pretty printing XML

class HtmlToXmlConverter:
    """
    A class to convert HTML strings to XML, designed with web framework
    functionalities in mind.

    Features:
    - Robust HTML parsing using BeautifulSoup.
    - Conversion to a well-formed XML structure.
    - Simple templating for data rendering (e.g., {{ variable }}).
    - Chaining methods for a fluent API.
    - Error handling for malformed HTML.
    - Pretty printing for XML output.
    """

    def __init__(self, html_string: str = ""):
        """
        Initializes the converter with an optional HTML string.

        Args:
            html_string (str): The initial HTML string to process.
        """
        self._html_string = html_string
        self._parsed_soup = None
        self._data_context = {}
        self._xml_root = None

    def load_html(self, html_string: str) -> 'HtmlToXmlConverter':
        """
        Loads a new HTML string into the converter.

        Args:
            html_string (str): The HTML string to load.

        Returns:
            HtmlToXmlConverter: The instance of the converter for chaining.
        """
        self._html_string = html_string
        self._parsed_soup = None  # Reset parsed soup
        self._xml_root = None     # Reset XML root
        return self

    def with_data(self, data: dict) -> 'HtmlToXmlConverter':
        """
        Sets the data context for rendering HTML templates.

        Args:
            data (dict): A dictionary of data to be used for templating.

        Returns:
            HtmlToXmlConverter: The instance of the converter for chaining.
        """
        self._data_context = data
        return self

    def render(self) -> 'HtmlToXmlConverter':
        """
        Renders the HTML string by replacing placeholders with data from the
        context. This is a simple templating mechanism.

        Placeholders are in the format {{ variable_name }}.

        Returns:
            HtmlToXmlConverter: The instance of the converter for chaining.
        """
        if not self._html_string:
            print("Warning: No HTML string loaded to render.")
            return self

        rendered_html = self._html_string
        for key, value in self._data_context.items():
            placeholder = r"{{\s*" + re.escape(key) + r"\s*}}"
            rendered_html = re.sub(placeholder, str(value), rendered_html)
        self._html_string = rendered_html
        return self

    def _parse_html(self):
        """
        Internal method to parse the HTML string using BeautifulSoup.
        Handles basic parsing errors.
        """
        if not self._html_string:
            raise ValueError("No HTML string provided for parsing.")
        try:
            # Using 'html.parser' for general HTML, 'lxml' or 'html5lib'
            # can be more robust for very malformed HTML if available.
            self._parsed_soup = BeautifulSoup(self._html_string, 'html.parser')
        except Exception as e:
            raise RuntimeError(f"Error parsing HTML: {e}")

    def _build_xml_element(self, soup_tag: Tag, parent_xml_element: ET.Element):
        """
        Recursively builds XML elements from BeautifulSoup tags.

        Args:
            soup_tag (bs4.Tag): The BeautifulSoup tag to convert.
            parent_xml_element (xml.etree.ElementTree.Element): The parent
                                                                XML element.
        """
        # Create the XML element with the tag name
        xml_element = ET.SubElement(parent_xml_element, soup_tag.name)

        # Add attributes
        for attr, value in soup_tag.attrs.items():
            # BeautifulSoup returns attribute values as lists for multi-valued
            # attributes like 'class'. Join them for XML.
            if isinstance(value, list):
                xml_element.set(attr, " ".join(value))
            else:
                xml_element.set(attr, str(value))

        # Process children (text and nested tags)
        for child in soup_tag.contents:
            if isinstance(child, NavigableString):
                # If it's a string, append it as text to the current XML element
                # Strip whitespace from text nodes to avoid empty text nodes
                # unless they contain significant content.
                text = str(child).strip()
                if text:
                    if xml_element.text is None:
                        xml_element.text = text
                    else:
                        xml_element.text += text # Append if text already exists
            elif isinstance(child, Tag):
                # If it's another tag, recurse
                self._build_xml_element(child, xml_element)

    def to_xml(self, pretty_print: bool = False) -> str:
        """
        Converts the loaded and potentially rendered HTML to an XML string.

        Args:
            pretty_print (bool): If True, the XML output will be
                                 formatted with indentation.

        Returns:
            str: The XML representation of the HTML.

        Raises:
            ValueError: If no HTML string is loaded.
            RuntimeError: If there's an error during HTML parsing or XML conversion.
        """
        if not self._html_string:
            raise ValueError("No HTML string loaded. Use load_html() first.")

        # Ensure HTML is parsed
        if self._parsed_soup is None:
            self._parse_html()

        # Create a dummy root element for the XML tree if HTML has multiple top-level elements
        # or if we want a consistent root.
        # In a real framework, you might decide on a specific root element like <document> or <template>.
        self._xml_root = ET.Element("root") # Using 'root' as a generic container

        # Iterate through the top-level children of the parsed HTML body
        # or the entire soup if no body is found (e.g., for fragments)
        if self._parsed_soup.body:
            elements_to_convert = self._parsed_soup.body.contents
        else:
            # Handle cases where HTML might be a fragment without <body>
            elements_to_convert = self._parsed_soup.contents

        for element in elements_to_convert:
            if isinstance(element, Tag):
                self._build_xml_element(element, self._xml_root)
            elif isinstance(element, NavigableString):
                text = str(element).strip()
                if text:
                    # If top-level text, add it to the root's text or create a text element
                    if self._xml_root.text is None:
                        self._xml_root.text = text
                    else:
                        self._xml_root.text += text # Append if text already exists

        # Convert ElementTree to string
        if pretty_print:
            # Use minidom for pretty printing as ET's tostring is basic
            rough_string = ET.tostring(self._xml_root, 'utf-8')
            reparsed = minidom.parseString(rough_string)
            return reparsed.toprettyxml(indent="  ")
        else:
            return ET.tostring(self._xml_root, encoding='unicode')

    # --- Framework-like Extension Points ---

    def validate_xml(self) -> bool:
        """
        Placeholder for XML validation (e.g., against an XSD schema).
        In a real framework, this would involve more complex logic.

        Returns:
            bool: True if XML is valid (conceptually), False otherwise.
        """
        if self._xml_root is None:
            print("Warning: No XML generated yet to validate.")
            return False
        # For demonstration, we'll just check if it's not empty
        return len(self._xml_root) > 0 # Simple check if root has children

    def save_xml(self, filepath: str, pretty_print: bool = False):
        """
        Saves the generated XML to a file.

        Args:
            filepath (str): The path to the file where XML will be saved.
            pretty_print (bool): If True, saves with pretty indentation.
        """
        if self._xml_root is None:
            self.to_xml()

        xml_string = self.to_xml(pretty_print=pretty_print)
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(xml_string)
            print(f"XML successfully saved to {filepath}")
        except IOError as e:
            print(f"Error saving XML to file: {e}")

