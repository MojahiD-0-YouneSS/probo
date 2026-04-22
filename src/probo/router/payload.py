import hashlib
import json
from typing import Any, Self
from probo.router.global_cache import global_cache

class RouterPayload:
    """
    SSDOM Payload Handler (Modernized v1.3.4).
    Mirrors JS DOM functionalities by tracking component state changes
    via hashing. Now powered by ProboCache to prevent memory leaks!
    """

    __slots__ = (
        "payloads",
        "diff",
    )

    def __init__(self, **payloads: Any) -> None:
        """
        :param payloads: Key-value pairs where key is component ID and
                         value is the component object.
        """
        self.payloads = payloads
        self.diff = {}
        self._process_payloads(**payloads)

    def clear_cache(self):
        global_cache.clear()
        self.payloads.clear()
        self.diff.clear()
        return self
    def _generate_hash(self, content: str) -> str:
        """Creates a unique fingerprint for a component's rendered output."""
        return hashlib.md5(content.encode("utf-8")).hexdigest()

    def _process_payloads(self, **payloads):
        """
        Iterates through payloads, renders them, and checks the ProboCache.
        Only adds changed components to the final diff.
        """
        raw_payloads = payloads or self.payloads

        for cid, component in raw_payloads.items():
            # Render the component using ProboUI's rendering logic
            rendered_content = (
                component.render() if hasattr(component, "render") else str(component)
            )
            new_hash = self._generate_hash(rendered_content)

            cache_key = f"payload::{cid}"
            old_hash = global_cache.get(cache_key)

            # Check if state has changed
            if old_hash != new_hash:
                self.diff[cid] = {"content": rendered_content, "hash": new_hash}
                # Update the cache with the new state (e.g., 24 hour TTL to prevent infinite bloat)
                global_cache.set_cache(cache_key, new_hash, ttl=86400)

    def get_json_response(self) -> str:
        """Returns only the components that have changed in JSON format."""
        return json.dumps(
            {"status": "update" if self.diff else "no-change", "payload": self.diff}
        )

    def get_xml_response(self) -> str:
        """Returns the changed components wrapped in an XML transport structure."""
        xml_fragments = []
        for cid, data in self.diff.items():
            xml_fragments.append(
                f'<component id="{cid}" hash="{data["hash"]}">{data["content"]}</component>'
            )

        return f'<ssdom_update>{"".join(xml_fragments)}</ssdom_update>'

    def load(self, **new_loads):
        """Dynamically loads new payloads for diffing."""
        self._process_payloads(**new_loads)
        return None

    def get_response(self, response_type: str) -> str:
        """Dynamically routes to the correct formatting function."""
        _allowed_formats = {
            "xml": self.get_xml_response,
            "json": self.get_json_response,
        }
        func = _allowed_formats.get(response_type, self.get_json_response)
        return func()
