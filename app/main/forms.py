from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, EqualTo


class FormLogin(Form):
    '''A class to instantiate wtf forms'''
    email = StringField('Email', 
        validators=[Required(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')


class RegistrationForm(Form):
    
    username = StringField('Username', 
        validators=[Required(), Length(1, 64)])
    email = StringField('Email', 
        validators=[Required(), Length(1, 64), Email()])

    password = PasswordField('Password', 
        validators=[Required(), EqualTo('password_cfm', 
            message='Please enter similar passwords.')])
    password_cfm = PasswordField('Confirm password', 
        validators=[Required()])
    submit = SubmitField('Sign up')

    def verify_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError('The email already exists.')

    def verify_username(self, username):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError('Username taken already. Try another.')