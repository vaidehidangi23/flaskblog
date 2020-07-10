from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ba930f6131829c8f7d97c87d6ce27e6d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db =SQLAlchemy(app)

from flaskblog import routes
