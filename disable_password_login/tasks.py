import frappe
from frappe.utils.password import update_password


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
    update_password(doc.namae, "")
    return True