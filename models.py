# @Time    : 2020/1/14 14:30
# @Author  : 帅气的陈小陌
# @Email   : 13784197113@163.com
# File     : models.py
# Software : PyCharm
from database import db


class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))

    def __init__(self, username, password):
        self.username = username
        self.password = password
