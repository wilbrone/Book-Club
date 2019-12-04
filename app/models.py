from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime

from . import login_manager
from . import db

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), index = True)
    full_name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))

    book = db.relationship('Books', backref ='user', lazy = 'dynamic')


    def save_user(self):
        db.session.add(self)
        db.session.commit()


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'


class Books(db.Model):
    """docstring for Books."""
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    author = db.Column(db.String(255))
    description = db.Column(db.String(255))
    posted = db.Column(db.DateTime, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    photo = db.Column(db.String)

    def save_book(self):
        db.session.add(self)
        db.session.commit()
