from flask import render_template, session, url_for, Response
from . import main
from .. import active
from forms import FormLogin


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/home')
def home():
    return render_template('home.html')


# @main.route('/online')
# def see_online():
#     return Response('Online: %s' % ', '.join(active.get_online_users()),
#                     mimetype='text/plain')
