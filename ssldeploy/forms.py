from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm):
    user_login_email = StringField('Company Email', validators=[DataRequired(),Email()])
    user_login_password = PasswordField('Company Password',validators=[DataRequired()])
    user_login_rememberme = BooleanField('Remember Me')
    user_login_submit = SubmitField('Sign In')