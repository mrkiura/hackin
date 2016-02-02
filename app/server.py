import os
from flask import Flask, render_template
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email
from flask.ext.wtf import Form
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = '45gvt5&&/#62t77tgygaysg8dytu'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

# define app dependencies
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)


class FormLogin(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')


# data model respresentign many to many relationship.
unions = db.Table('unions',
                  db.Column('session_id', db.Integer,
                            db.ForeignKey('tbl_sessions.id')),
                  db.Column(
                      'user_id', db.Integer, db.ForeignKey('tbl_users.id'))
                  )


class CodeSessions(db.Model):
    '''a schema for storing a user's programming
    sessions '''

    __tablename__ = 'tbl_sessions'
    id = db.Column(db.Integer, primary_key=True)
    session_address = db.Column(db.String(250))

    def __repr__(self):
        return '<CodeSessions %r>' % self.session_address


class User(db.Model):
    '''a schema for storing user data'''

    __tablename__ = 'tbl_users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    hashed_pass = db.Column(db.String(128))
    sessions = db.relationship('CodeSessions',
                               secondary=unions,
                               backref=db.backref('users', lazy='dynamic'),
                               lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % self.username

    @property
    def password(self):
        raise AttributeError('password is not readable')

    @password.setter
    def password(self, password):
        self.hashed_pass = generate_password_hash(password)

    def verify_pass(self, password):
        return check_password_hash(self.hashed_pass, password)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def auth():
    form = FormLogin()
    return render_template('login.html', form=form)

if __name__ == '__main__':
    manager.run()
