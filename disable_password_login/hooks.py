import frappe
from . import __version__ as app_version

app_name = "disable_password_login"
app_title = "Disable Password Login"
app_publisher = "IoTReady"
app_description = "Disallow Password Login If Social Login Is Enabled"
app_email = "hello@iotready.co"
app_license = "MIT"


def disable_password(doc, event):
    assert doc.doctype == 'User', "Only valid for User doctype"
    if not frappe.db.count('Social Login Key', filters={'enable_social_login': 1}) > 0:
        return False
    config = frappe.get_doc('Disable Password Login Settings', '')
    if not config.disable_password_login:
        return False
    allowed_users = [row.user for row in config.allow_password_login_table]
    if doc.name == 'Administrator' or doc.name in allowed_users:
        return False
    doc.password = None
    return True
        

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    "User": {
        "on_update": "disable_password_login.hooks.disable_password",
    }
}
