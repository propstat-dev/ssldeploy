from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, ValidationError
from wtforms.validators import DataRequired, Email

# User Log-in form for self-service portal
class UserLoginForm(FlaskForm):
    user_login_username = StringField('Company Email', validators=[DataRequired(),Email()])
    user_login_password = PasswordField('Company Password',validators=[DataRequired()])
    user_login_rememberme = BooleanField('Remember Me')
    user_login_submit = SubmitField('Sign In')

# Admin Log-in form for admin interface
class AdminLoginForm(FlaskForm):
    admin_login_username = StringField('Admin User', validators=[DataRequired()])
    admin_login_password = PasswordField('Admin Password', validators=[DataRequired()])
    admin_login_rememberme = BooleanField('Remember Me')
    # Currently only PAM, for future use when we add LDAP/AD support can be enabled to selectable realms
    admin_login_realm_options = [
        ("pam", "Linux PAM Standard Authentication"),
        ("ldap", "LDAP"),
        ("ad", "Active Directory"),
    ]
    admin_login_realms_enabled = {"pam"}  # only PAM is allowed for now, but this can be easily extended in the future

    admin_login_realm = SelectField(
        "Authentication Realms",
        choices=admin_login_realm_options,
        validators=[DataRequired()]
    )

    admin_login_submit = SubmitField('Sign In')

    def validate_admin_realm(self, field):
        if field.data not in self.admin_login_realms_enabled:
            raise ValidationError("Selected authentication method is not enabled.")