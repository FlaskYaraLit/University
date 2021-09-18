from flask import render_template
from config import app

class UniverController(object):
    @staticmethod
    @app.route('/univer/history')
    def history():
        return render_template('univer/history.html')

    @staticmethod
    @app.route('/univer/photos')
    def photos():
        return render_template('univer/photos.html')

    @staticmethod
    @app.route('/univer/rector')
    def rector():
        return render_template('univer/rector.html')
