import xml.etree.ElementTree as ET
from probo.xml.xml import HtmlToXmlConverter

class TemplateResolver:
    """A structural parser that extracts and merges HTML attributes for JIT styling.

    TemplateResolver serves as the "Intelligence" layer for the styling engine. 
    It converts HTML strings into XML trees, traverses the nodes, and builds a 
    registry of tags, classes, and attributes. This registry is then used to 
    validate that proposed CSS selectors actually exist within the template, 
    preventing "Ghost Styles" from bloating the final CSS payload.

    Attributes:
        tmplt_str (str): The raw HTML source string to be resolved.
        template_attributes (dict): An inverted map of attribute names to lists 
            of unique values found in the template.
        load_it (bool): Flag to determine if the resolver should automatically 
            populate internal state during execution.
        template_info (dict): A mapping of tags to their merged attribute dictionaries.
        template_tags (list): A list of all unique HTML tags found in the template.
    """
    __slots__ = (
        'tmplt_str',
        'template_attributes',
        'load_it',
        'template_info',
        'template_tags',
    )
    def __init__(self, tmplt_str=None, load_it=False):
        self.tmplt_str = tmplt_str
        self.template_attributes = {}
        self.load_it = load_it
        self.template_info = {}
        self.template_tags = []


    def parse_xml(self, xml_string: str) -> ET.Element:
        """Parses a valid XML string into an ElementTree root.

        Args:
            xml_string (str): The XML-formatted string.

        Returns:
            ET.Element: The root element of the parsed XML tree.
        """
        return ET.fromstring(xml_string)

    def merge_attributes(self, existing_attrs: dict, new_attrs: dict) -> dict:
        """Merges two sets of attributes, with special handling for CSS classes.

        If a 'class' attribute exists in both dictionaries, the classes are 
        merged into a unique, space-separated string. All other attributes 
        in 'new_attrs' will override values in 'existing_attrs'.

        Args:
            existing_attrs (dict): The current attribute collection.
            new_attrs (dict): The incoming attributes to merge or override.

        Returns:
            dict: The merged attribute dictionary.
        """
        for key, value in new_attrs.items():
            if key == "class":
                # Merge class lists uniquely
                existing_classes = set(existing_attrs.get("class", "").split())
                new_classes = set(value.split())
                existing_attrs["class"] = " ".join(
                    existing_classes.union(new_classes)
                ).strip()
            else:
                # Override or add new attributes
                existing_attrs[key] = value
        return existing_attrs

    def collect_elements_attributes(self, root: ET.Element, load_it=False) -> dict:
        """Traverses the XML tree to collect and merge attributes for all tags.

        This method ignores the 'root' wrapper tag and performs a deep 
        traversal of the tree, aggregating attributes for every unique 
        HTML tag encountered.

        Args:
            root (ET.Element): The XML root element to begin traversal.
            load_it (bool): If True, populates `self.template_tags`.

        Returns:
            dict: A dictionary mapping tag names to their merged attributes.
        """
        result = {}

        def _traverse(elem):
            if elem.tag != "root":
                # Merge attributes for same tags
                if load_it:
                    self.template_tags.append(elem.tag)
                if elem.tag not in result:
                    result[elem.tag] = elem.attrib.copy()

                else:
                    result[elem.tag] = self.merge_attributes(
                        result[elem.tag], elem.attrib
                    )

            for child in elem:
                _traverse(child)

        _traverse(root)

        return result

    def xml_to_tag_dict(self, xml_string: str) -> dict:
        """Converts an XML string into a dictionary of merged tag attributes.

        Args:
            xml_string (str): The XML data.

        Returns:
            dict: The resolved tag dictionary.
        """
        root = self.parse_xml(xml_string)
        return self.collect_elements_attributes(root)

    def invert_tag_attribute_dict(self, tag_dict: dict, unique: bool = True, split_classes: bool = True) -> dict:
        """Inverts the tag-first dictionary into an attribute-first mapping.

        Converts {tag: {attr: value}} into {attr: [values...]}. This is 
        essential for the styling engine to quickly check if a specific 
        CSS class or ID exists anywhere in the template.

        Args:
            tag_dict (dict): The resolved tag-attribute dictionary.
            unique (bool): If True, duplicate values are removed from the lists.
            split_classes (bool): If True, 'class' strings are split into 
                individual tokens.

        Returns:
            dict: A mapping of attribute names to lists of their values.
        """
        result = {}

        for tag, attrs in tag_dict.items():
            for attr, value in attrs.items():
                if not value:
                    continue

                # Split class values into individual tokens
                if split_classes and attr == "class":
                    values = value.split()
                else:
                    values = [value]

                # Initialize attribute list
                if attr not in result:
                    result[attr] = []

                result[attr].extend(values)

        # Make unique if requested
        if unique:
            result = {
                k: list(dict.fromkeys(v)) for k, v in result.items()
            }  # preserves order

        return result

    def __template_resolver(self, tmplt_str=None, load_it=False):
        """Internal execution pipeline for template resolution.

        Performs the HTML -> XML conversion and triggers the attribute 
        extraction and inversion logic.

        Args:
            tmplt_str (str, optional): The template string to resolve.
            load_it (bool): Whether to update class-level state.

        Returns:
            dict: The final resolved tag-attribute mapping.
        """
        xml_data = HtmlToXmlConverter(str(tmplt_str)).to_xml()
        result = self.xml_to_tag_dict(xml_data)
        #        self.template_info = result
        if load_it:
            self.template_tags = list(set(self.template_tags))

            self.template_attributes.update(self.invert_tag_attribute_dict(result))

        return result

    def template_resolver(self, template=None, load_it=False):
        """Public entry point for resolving templates.

        Args:
            template (str, optional): An external template to resolve. 
                If None, uses `self.tmplt_str`.
            load_it (bool): Whether to update class-level state.

        Returns:
            dict: The resolved template information.
        """
        if template:
            return self.__template_resolver(template, load_it)
        else:
            info = self.__template_resolver(
                tmplt_str=self.tmplt_str, load_it=self.load_it
            )
            self.template_info.update(info)
            return info
