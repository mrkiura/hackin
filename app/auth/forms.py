from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo


class FormLogin(Form):
    '''A form to authenticate users'''
    email = StringField('Email',
                        validators=[Required(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me signed in')
    submit = SubmitField('Log In')


class FormSignUp(Form):
    '''a form to sign up users'''
    email = StringField('Email',
                        validators=[Required(), Length(1, 64), Email()])
    username = StringField('Username', validators=[
        Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Usernames must have only letters, '
                                          'numbers, dots or underscores')])
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
