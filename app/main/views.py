from flask import render_template, session, redirect, url_for
from . import main
from forms import FormLogin

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/login', methods=['GET', 'POST'])
def auth():
    form = FormLogin()
    return render_template('login.html', form=form)

