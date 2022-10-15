## Disable Password Login

Disallow Password Login If Social Login Is Enabled

### Use Case

- You want to only allow social auth and disallow password based authentication.


### How Does It Work?

- Uses an `on_update` hook on the `User` doctype to reset the User password. 
- This ensures that even if the user does navigate to the reset password page, the password can't be used to login.
- You can disable the app completely or for specific users by going to the "Disable Password Login Settings" configuration page.

#### License

MIT