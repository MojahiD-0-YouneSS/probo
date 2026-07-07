import sys
from probo.styles.plain_css import CssSelector
from probo.utility import exists_in_dict

html_str = '<div class="user-card"><span class="user-name">Alice</span><span class="user-status" id="status-1">Active</span></div>'
info = CssSelector(html_str).template_info
print("TEMPLATE_INFO:")
print(info)

print("EXISTS user-name:", exists_in_dict(info, "user-name"))
print("EXISTS user-card:", exists_in_dict(info, "user-card"))
print("EXISTS user-status:", exists_in_dict(info, "user-status"))
