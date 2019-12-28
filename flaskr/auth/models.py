from flask_login import UserMixin
from sqlalchemy import Column, Integer, String

from .. import db


class User(UserMixin, db.Model):
    __tablename__ = 'site_user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.username)
