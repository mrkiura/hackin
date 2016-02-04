import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    '''class containing config variables
    '''

    SECRET_KEY = '45gvt5&&/#62t77tgygaysg8dytu'
    SQLALCHEMY_DATABASE_URI = \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True


    @staticmethod
    def init_app(app):
        pass


config = {
    'default': Config
}
