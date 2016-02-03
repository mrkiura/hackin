from flask import render_template, redirect, request, url_for, flash
from . import auth
from .forms import FormLogin
from flask.ext.login import login_user, logout_user, login_required
from ..models import User



@auth.route('/login', methods=['GET', 'POST'])
def authenticate():
    form = FormLogin()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_pass(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.home'))
        flash('Invalid username or password.')
    return render_template('authentication/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have successfully logged out.')
    return redirect(url_for('main.index'))
