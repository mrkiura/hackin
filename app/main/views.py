from flask import render_template, session, url_for, Response, redirect
from . import main
from .. import active
from forms import FormLogin, NewSession
from .. import db
from ..models import CodeSessions, User
from app import login_mgr
from flask.ext.login import login_user, logout_user, login_required, current_user

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/home')
def home():
    return render_template('home.html')


@main.route('/sessions')
def sessions():
    return render_template('sessions.html')


@main.route('/new', methods=['GET', 'POST'])
def new_session():
    form = NewSession()
    if form.validate_on_submit():
        session_ = CodeSessions(session_name=form.session_name.data, 
            session_lang=form.language.data)
        user_ = User.query.get(current_user.id)
        user_.sessions.append(session_)
        db.session.add(user_)
        db.session.commit()
        id_ = session_.id
        return render_template('sessions.html', id_=id_)
    return render_template('add_session.html', form=form)


