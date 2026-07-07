from probo import DIV, SPAN, P, A
from probo.components import Component
from probo.components.light_tags import Ldiv, Lspan
from probo.context.context_logic import loop

# 1. UserCard Component
class UserCard(Component):
    def __init__(self, user: dict):
        self.user = user
        template = DIV(
            SPAN(self.user["name"], Class="user-name"),
            SPAN(self.user["status"], Class="user-status", Id=f"status-{self.user['id']}"),
            Class="user-card"
        )
        super().__init__("UserCard", template=template)
        
        from probo.styles.plain_css import CssRule, CssSelector
        rules = {
            CssSelector().cls("user-card").render(): CssRule(border="1px solid #ccc", padding="10px", margin_bottom="5px").declarations,
            CssSelector().cls("user-name").render(): CssRule(font_weight="bold").declarations,
            CssSelector().cls("user-status").render(): CssRule(color="green").declarations
        }
        self.load_css_rules(**rules)

# 2. UserList Component
class UserList(Component):
    def __init__(self, users: list):
        self.users = users
        
        rendered_cards = []
        bubbled_css = []
        for u in self.users:
            card = UserCard(u)
            rendered_cards.append(card.template_obj)
            bubbled_css.extend(card.active_css_rules)
            
        template = DIV(
            *rendered_cards,
            Class="user-list",
            Id="main-user-list"
        )
        super().__init__("UserList", template=template)
        self.active_css_rules.extend(bubbled_css)

# 3. Dashboard Component
class DashboardComponent(Component):
    def __init__(self, title: str, users: list):
        self.title = title
        self.users = users
        
        user_list = UserList(self.users)
        
        template = DIV(
            Ldiv(
                SPAN(self.title, Class="dashboard-title"),
                # HTMX attribute injection
                A("Reload", Hx_get="/api/reload", Hx_swap="outerHTML", Class="reload-btn"),
                Id="dashboard-header"
            ),
            user_list.template_obj,
            Id="dashboard-main"
        )
        super().__init__("DashboardComponent", template=template)
        self.active_css_rules.extend(user_list.active_css_rules)

# Test Fixtures / Data
USERS_DATA = [
    {"id": 1, "name": "Alice", "status": "Active"},
    {"id": 2, "name": "Bob", "status": "Inactive"},
]

def test_comprehensive_render():
    dashboard = DashboardComponent("Admin Dashboard", USERS_DATA)
    output = dashboard.render()[0] # render returns html, css tuple usually
    
    assert "Admin Dashboard" in output
    assert "Alice" in output
    assert "Bob" in output
    assert "hx-get=\"/api/reload\"" in output
    assert "hx-swap=\"outerHTML\"" in output
    assert "<div" in output
    assert "<span" in output

def test_comprehensive_css_bubbling():
    dashboard = DashboardComponent("Admin Dashboard", USERS_DATA)
    _, css = dashboard.render() # Process tree
    
    # Ensure rules bubbled up properly
    assert ".user-card" in css
    assert ".user-name" in css
    assert ".user-status" in css

def test_comprehensive_ssdom_queries():
    dashboard = DashboardComponent("Admin Dashboard", USERS_DATA)
    # SSDOM queries operate on the internal object tree.
    # We query the contiguous template nodes starting from the dashboard root.
    
    main_list = dashboard.template_obj.css_selector("#main-user-list")
    assert main_list is not None
    assert main_list.tag == "DIV"
    
    header = dashboard.template_obj.css_selector("#dashboard-header")
    assert header is not None
    
    status_node = dashboard.template_obj.css_selector("#status-1")
    assert status_node is not None
    assert status_node.tag == "SPAN"
    assert status_node.text == "Active"
    
    # query by class
    cards = dashboard.template_obj.css_selector_all(".user-card")
    assert len(cards) == 2
    
    titles = dashboard.template_obj.css_selector_all(".dashboard-title")
    assert len(titles) == 1
    assert titles[0].text == "Admin Dashboard"
    
    # query by tag
    spans = dashboard.template_obj.css_selector_all("span")
    # Title (1) + User Name (2) + User Status (2) = 5
    assert len(spans) == 5

def test_comprehensive_streaming():
    dashboard = DashboardComponent("Admin Dashboard", USERS_DATA)
    # stream returns chunks.
    stream_output = list(dashboard.template_obj.stream())
    
    full_string = "".join(str(chunk) for chunk in stream_output)
    
    assert "Admin Dashboard" in full_string
    assert "Alice" in full_string
    assert "hx-get=\"/api/reload\"" in full_string
