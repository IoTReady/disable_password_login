from . import __version__ as app_version

app_name = "disable_password_login"
app_title = "Disable Password Login"
app_publisher = "IoTReady"
app_description = "Disallow Password Login If Social Login Is Enabled"
app_email = "hello@iotready.co"
app_license = "MIT"
        

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    "User": {
        "on_update": "disable_password_login.tasks.disable_password",
    }
}
