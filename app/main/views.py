from flask import render_template, session, redirect, url_for
from . import main
from forms import FormLogin

@main.route('/')
def index():
    return render_template('index.html')
