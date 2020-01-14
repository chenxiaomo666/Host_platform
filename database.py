# @Time    : 2020/1/14 14:30
# @Author  : 帅气的陈小陌
# @Email   : 13784197113@163.com
# File     : database.py
# Software : PyCharm
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


def db_init():
    db.create_all()


from models import User
