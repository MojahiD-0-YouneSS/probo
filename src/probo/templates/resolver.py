import xml.etree.ElementTree as ET
from src.probo.xml.xml import HtmlToXmlConverter


class TemplateResolver:
    def __init__(self, tmplt_str=None, load_it=False):
        self.tmplt_str = tmplt_str
        self.template_attributes = {}
        self.load_it = load_it
        self.template_info = {}
        self.template_tags = []

    """ take template and process to css sylectors them eache added value to self selectors shall be tested if they exucted in the template first"""

    def parse_xml(self, xml_string: str) -> ET.Element:
        """Parse XML string and return the root element."""
        return ET.fromstring(xml_string)

    def merge_attributes(self, existing_attrs: dict, new_attrs: dict) -> dict:
        """Merge new attributes into existing ones (merge class names, override duplicates)."""
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
        """
        Traverse XML and collect tags with their merged attributes.
        Ignores the root tag itself.
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
        """Main function: XML → dict of tags → merged attributes."""
        root = self.parse_xml(xml_string)
        return self.collect_elements_attributes(root)

    def invert_tag_attribute_dict(
        self, tag_dict: dict, unique: bool = True, split_classes: bool = True
    ) -> dict:
        """
        Invert {tag: {attr: value}} into {attr: [values...]}.

        Args:
            tag_dict (dict): dict of tags and their attributes
            unique (bool): if True, remove duplicate values
            split_classes (bool): if True, split 'class' attributes into separate tokens

        Returns:
            dict: attribute → list of all values
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
        xml_data = HtmlToXmlConverter(str(tmplt_str)).to_xml()
        result = self.xml_to_tag_dict(xml_data)
        #        self.template_info = result
        if load_it:
            self.template_tags = list(set(self.template_tags))

            self.template_attributes.update(self.invert_tag_attribute_dict(result))

        return result

    def template_resolver(self, template=None, load_it=False):
        if template:
            return self.__template_resolver(template, load_it)
        else:
            info = self.__template_resolver(
                tmplt_str=self.tmplt_str, load_it=self.load_it
            )
            self.template_info.update(info)
            return info
