import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    '''class containing config variables
    '''

    SECRET_KEY = '45gvt5&&/#62t77tgygaysg8dytu'
    SQLALCHEMY_DATABASE_URI = \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'nullpointer16'
    MAIL_PASSWORD = 'jcqvollzkglkpuoe'
    MAIL_SENDER = 'Admin <nullpointer16@gmail.com>'


    @staticmethod
    def init_app(app):
        pass


config = {
    'default': Config
}
