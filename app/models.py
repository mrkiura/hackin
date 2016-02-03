from . import db
from flask.ext.login import UserMixin
from . import login_mgr
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


class User(UserMixin, db.Model):
    '''a schema for storing user data'''

    __tablename__ = 'tbl_users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
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

    @login_mgr.user_loader
    def load_user(user_id):
      return User.query.get(int(user_id))