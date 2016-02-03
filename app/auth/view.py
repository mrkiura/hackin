from flask import render_template
from . import auth


@auth.route('/login', methods=['GET', 'POST'])
def authenticate():
    # form = FormLogin()
    return render_template('authentication/login.html') #form=form)
