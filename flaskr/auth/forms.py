from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, SubmitField, TextField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = TextField(
        'Username', validators=[DataRequired(), Length(1, 50)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    login = SubmitField('Log in')


class RegisterForm(FlaskForm):
    username = TextField(
        'Username', validators=[DataRequired(), Length(1, 50)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm = PasswordField(
        'Confirm password', validators=[DataRequired()])
    register = SubmitField('Register')
