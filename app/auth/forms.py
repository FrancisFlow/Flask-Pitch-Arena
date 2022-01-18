from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import Required, Email, EqualTo

from ..models import User




class RegistrationForm(FlaskForm):

    email = StringField("Enter your email address", validators=[Required])
    username = StringField("Username", validators=[Required])
    password = PasswordField('Password', validators = [Required])
    submit = SubmitField('Sign up')

    def validate_email(self, data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('An account exists for this email')

    def validate_username(self, data_field):

        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('Username already exists')



class LoginForm(FlaskForm):
     email = StringField("Your Email Address", validators=[Required])
     password = PasswordField("Password", validators = [Required])

     remember = BooleanField('Remember me')
     submit = SubmitField('Sign In')