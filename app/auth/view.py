from flask import render_template, redirect, request, \
    url_for, flash
from . import auth
from .forms import FormLogin, FormSignUp
from flask.ext.login import login_user, logout_user, login_required, current_user
from ..models import User
from .. import db
from flask import session
from firebase import Firebase


@auth.route('/login', methods=['GET', 'POST'])
def authenticate():
    fb = Firebase('https://hack-in.firebaseio.com/users')

    form = FormLogin()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_pass(form.password.data):
            login_user(user, form.remember_me.data)
            rfb = fb.push({'user_id': user.username, 'email': user.email})
            return redirect(request.args.get('next') or url_for('main.home'))
        flash('Invalid username or password.')
    return render_template('authentication/login.html',
                           form=form, session=session)


@auth.route('/logout')
@login_required
def logout():
    fb = Firebase('https://hack-in.firebaseio.com/users')
    logout_user()
    flash('You have successfully logged out.')
    return redirect(url_for('main.index'))


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = FormSignUp()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account successfuly created. Please login')
        return redirect(url_for('auth.authenticate'))
    return render_template('authentication/login.html', form=form)
