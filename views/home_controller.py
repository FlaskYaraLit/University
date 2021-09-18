from flask import render_template
from config import app

class HomeController(object):

    @staticmethod
    @app.route("/")
    def index():
        return render_template('home/index.html')

    @staticmethod
    @app.route('/faculty')
    def about():
        return render_template('home/faculty.html')

    @staticmethod
    @app.route('/abitur')
    def contact():
        return render_template('home/abitur.html')
