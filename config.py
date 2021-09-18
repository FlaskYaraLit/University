from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY']='202cb962ac59075b964b07152d234b70'
app.config['TEMPLATES_AUTO_RELOAD'] = True

