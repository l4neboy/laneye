from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class Item(db.Model):
    __tablename__ = 'newtable'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    #    text = db.Column(db.Text, nullable=False)

    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __repr__(self):
        return self.title

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name

    def __repr__(self):
        return self.name


class BookModel(db.Model):
    __tablename__ = 'books'
 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Integer())
    author = db.Column(db.String(80))
 
    def __init__(self, name, price, author):
        self.name = name
        self.price = price
        self.author = author 
     
    def json(self):
        return {"name":self.name, "price":self.price, "author":self.author}
