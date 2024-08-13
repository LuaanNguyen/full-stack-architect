from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = ["sqlite:///mydatabase.db"] #specifying the address of the database
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #disable track modifications


db = SQLAlchemy(app)



