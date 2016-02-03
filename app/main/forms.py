from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, EqualTo


class FormLogin(Form):
    '''A class to instantiate wtf forms'''
    email = StringField('Email', 
        validators=[Required(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me signed in')
    submit = SubmitField('Log In')


