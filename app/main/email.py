from flask import current_app, render_template, redirect
from flask.ext.mail import Message
from threading import Thread
from .. import mail 



def send_mail_conc(app, msg):
    '''Uses a worker thread to send mail
    '''
    with app.app_context():
        mail.send(msg)


def send_email(subj, content, to, **kwargs):
    app = current_app._get_current_object()
    msg = Message(subj,
                  sender=app.config['MAIL_SENDER'], recipients=[to])
    msg.body = content['body']
    msg.html = content['html']
    t = Thread(target=send_mail_conc, args=[app, msg])
    t.start()
    return t
