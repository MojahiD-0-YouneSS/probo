from probo import(
    G,
    DEFS,
    TEXT,
    TSPAN,
    SVG,
    SYMBOL,
    MARKER,
    PATTERN,
    MASK,
    CLIPPATH,
    LINEARGRADIENT,
    RADIALGRADIENT,
    FILTER,
    FECOMPONENTTRANSFER,
    FEDIFFUSELIGHTING,
    FEMERGE,
    FESPECULARLIGHTING,
    ANIMATEMOTION,
    FOREIGNOBJECT,
    PATH,
    CIRCLE,
    RECT,
    LINE,
    POLYLINE,
    POLYGON,
    ELLIPSE,
    IMAGE,
    FEBLEND,
    FECOLORMATRIX,
    FECOMPOSITE,
    FECONVOLVEMATRIX,
    FEDISPLACEMENTMAP,
    FEDROPSHADOW,
    FEFLOOD,
    FEFUNCA,
    FEFUNCB,
    FEFUNCG,
    FEFUNCR,
    FEGAUSSIANBLUR,
    FEIMAGE,
    FEMERGENODE,
    FEMORPHOLOGY,
    FEOFFSET,
    FEPOINTLIGHT,
    FESPOTLIGHT,
    FETILE,
    FETURBULENCE,
    ANIMATE,
    ANIMATETRANSFORM,
    SET,
    VIEW,
    USE,
    STOP,
)

import pytest

# Note: Ensure BaseHTMLElement, ElementNodeMixin, and Element 
# are imported or defined before running this.

@pytest.mark.parametrize("element_class, expected_tag, is_self_closing", [
    # --- Content Elements ---
    (G, "g", False),
    (DEFS, "defs", False),
    (TEXT, "text", False),
    (TSPAN, "tspan", False),
    (SVG, "svg", False),
    (SYMBOL, "symbol", False),
    (MARKER, "marker", False),
    (PATTERN, "pattern", False),
    (MASK, "mask", False),
    (CLIPPATH, "clipPath", False),
    (LINEARGRADIENT, "linearGradient", False),
    (RADIALGRADIENT, "radialGradient", False),
    (FILTER, "filter", False),
    (FECOMPONENTTRANSFER, "feComponentTransfer", False),
    (FEDIFFUSELIGHTING, "feDiffuseLighting", False),
    (FEMERGE, "feMerge", False),
    (FESPECULARLIGHTING, "feSpecularLighting", False),
    (ANIMATEMOTION, "animateMotion", False),
    (FOREIGNOBJECT, "foreignObject", False),
    
    # --- Self-Closing Elements ---
    (PATH, "path", True),
    (CIRCLE, "circle", True),
    (RECT, "rect", True),
    (LINE, "line", True),
    (POLYLINE, "polyline", True),
    (POLYGON, "polygon", True),
    (ELLIPSE, "ellipse", True),
    (IMAGE, "image", True),
    (FEBLEND, "feBlend", True),
    (FECOLORMATRIX, "feColorMatrix", True),
    (FECOMPOSITE, "feComposite", True),
    (FECONVOLVEMATRIX, "feConvolveMatrix", True),
    (FEDISPLACEMENTMAP, "feDisplacementMap", True),
    (FEDROPSHADOW, "feDropShadow", True),
    (FEFLOOD, "feFlood", True),
    (FEFUNCA, "feFuncA", True),
    (FEFUNCB, "feFuncB", True),
    (FEFUNCG, "feFuncG", True),
    (FEFUNCR, "feFuncR", True),
    (FEGAUSSIANBLUR, "feGaussianBlur", True),
    (FEIMAGE, "feImage", True),
    (FEMERGENODE, "feMergeNode", True),
    (FEMORPHOLOGY, "feMorphology", True),
    (FEOFFSET, "feOffset", True),
    (FEPOINTLIGHT, "fePointLight", True),
    (FESPOTLIGHT, "feSpotLight", True),
    (FETILE, "feTile", True),
    (FETURBULENCE, "feTurbulence", True),
    (ANIMATE, "animate", True),
    (ANIMATETRANSFORM, "animateTransform", True),
    (SET, "set", True),
    (VIEW, "view", True),
    (USE, "use", True),
    (STOP, "stop", True),
])
def test_svg_element_rendering(element_class, expected_tag, is_self_closing):
    """
    Parametrized test to verify class instantiation and tag rendering.
    """
    test_id = "test_item_123"
    
    # 1. Instantiate based on the class signature type
    if is_self_closing:
        # Signature: def __init__(self, **kwargs)
        instance = element_class(Id=test_id)
    else:
        # Signature: def __init__(self, *content, **attrs)
        instance = element_class("content_placeholder", Id=test_id)
    
    # 2. Render to get the element object/string
    # Depending on your 'probo' framework, .element might be a string or object.
    # We assume .render() returns a structure containing the tag name.
    result = instance.render()
    
    # 3. Assertions
    # If render() returns a string, we check the string. 
    # If it returns an object with a .tag property, check that.
    rendered_str = str(result)
    
    assert expected_tag in rendered_str, f"Expected tag <{expected_tag}> not found in: {rendered_str}"
    assert test_id in rendered_str, f"Attribute 'id' not found in: {rendered_str}"

