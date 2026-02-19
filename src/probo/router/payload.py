import hashlib
import json

class RouterPayload:
    """
    SSDOM Payload Handler.
    Mirrors JS DOM functionalities by tracking component state changes 
    via hashing and TCM integration.
    """
    # Simple in-memory cache for hashing. In production, use Redis or Django Cache.
    _state_cache = {}

    def __init__(self, **payloads) -> None:
        """
        :param payloads: Key-value pairs where key is component ID and 
                         value is the component object (tcm-based).
        """
        self.payloads = payloads
        self.diff = {}
        self._process_payloads()

    def _generate_hash(self, content: str) -> str:
        """Creates a unique fingerprint for a component's rendered output."""
        return hashlib.md5(content.encode()).hexdigest()

    def _process_payloads(self,**payloads):
        """
        Iterates through payloads, renders them, and checks the cache.
        Only adds changed components to the final diff.
        """
        raw_payloads = payloads or self.payloads
        for cid, component in raw_payloads.items():
            # Render the component using ProboUI's rendering logic
            rendered_content = component.render() if hasattr(component, 'render') else str(component)
            new_hash = self._generate_hash(rendered_content)
            
            # Check if state has changed
            if self._state_cache.get(cid) != new_hash:
                self.diff[cid] = {
                    "content": rendered_content,
                    "hash": new_hash
                }
                # Update the cache with the new state
                self._state_cache[cid] = new_hash

    def get_json_response(self) -> str:
        """Returns only the components that have changed in JSON format."""
        return json.dumps({
            "status": "update" if self.diff else "no-change",
            "payload": self.diff
        })

    def get_xml_response(self) -> str:
        """Returns the changed components wrapped in an XML transport structure."""
        xml_fragments = []
        for cid, data in self.diff.items():
            xml_fragments.append(f'<component id="{cid}" hash="{data["hash"]}">{data["content"]}</component>')
        
        return f'<ssdom_update>{"".join(xml_fragments)}</ssdom_update>'

    def load(self,**new_loads):
        self._process_payloads(**new_loads)
        return None

    def get_response(self, response_type):
        _allowed_formats = {
            'xml':self.get_xml_response,
            'json':self.get_json_response,
        }
        func = _allowed_formats.get(response_type,)
        return func()

