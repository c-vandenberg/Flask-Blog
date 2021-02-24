

from flask_wtf import FlaskForm

# wtforms library has form fields for usernames (e.g. StringField), passwords (e.g. PasswordField) and submit buttons (e.g. SubmitField)
from wtforms import StringField, PasswordField, SubmitField, BooleanField

# wtforms.validators library allows for form validation
# DataRequired validator ensures forms cannot be empty
# Length validator ensures string must be of certain length
# Email validator ensures email given is valid
# EqualTo validator ensures strings match
from wtforms.validators import DataRequired, Length, Email, EqualTo
import email_validator

# Class for registration form for users to register
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')

# Class for login form for users to login
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember =  BooleanField('Remember Me')
    submit = SubmitField('Login')