from . import __version__ as app_version

app_name = "disable_password_login"
app_title = "Disable Password Login"
app_publisher = "IoTReady"
app_description = "Disallow Password Login If Social Login Is Enabled"
app_email = "hello@iotready.co"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/disable_password_login/css/disable_password_login.css"
# app_include_js = "/assets/disable_password_login/js/disable_password_login.js"

# include js, css files in header of web template
# web_include_css = "/assets/disable_password_login/css/disable_password_login.css"
# web_include_js = "/assets/disable_password_login/js/disable_password_login.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "disable_password_login/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "disable_password_login.utils.jinja_methods",
# 	"filters": "disable_password_login.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "disable_password_login.install.before_install"
# after_install = "disable_password_login.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "disable_password_login.uninstall.before_uninstall"
# after_uninstall = "disable_password_login.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "disable_password_login.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"disable_password_login.tasks.all"
# 	],
# 	"daily": [
# 		"disable_password_login.tasks.daily"
# 	],
# 	"hourly": [
# 		"disable_password_login.tasks.hourly"
# 	],
# 	"weekly": [
# 		"disable_password_login.tasks.weekly"
# 	],
# 	"monthly": [
# 		"disable_password_login.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "disable_password_login.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "disable_password_login.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "disable_password_login.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"disable_password_login.auth.validate"
# ]

# Translation
# --------------------------------

# Make link fields search translated document names for these DocTypes
# Recommended only for DocTypes which have limited documents with untranslated names
# For example: Role, Gender, etc.
# translated_search_doctypes = []
