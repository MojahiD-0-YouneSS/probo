import pytest
from probo.components.elements import Head

def test_csp_meta_tag():
    """16. Content Security Policy."""
    h = Head()
    h.register_meta(http_equiv="content-security-policy", content="default-src 'self'")
    assert 'http-equiv="content-security-policy"' in h.render()

def test_x_frame_options():
    """17. X-Frame-Options."""
    h = Head()
    h.register_meta(http_equiv="content-language", content="DENY")
    assert 'content="DENY"' in h.render()

def test_referrer_policy():
    """18. Referrer Policy."""
    h = Head()
    h.register_meta(name="referrer", content="no-referrer")
    assert 'name="referrer"' in h.render()

def test_viewport_config():
    """19. Strict Viewport."""
    h = Head()
    h.register_meta(name="viewport", content="width=device-width, initial-scale=1, user-scalable=no")
    assert "user-scalable=no" in h.render()

def test_charset_utf8():
    """20. Charset."""
    h = Head()
    h.register_meta(charset="UTF-8")
    assert '<meta charset="UTF-8"' in h.render()