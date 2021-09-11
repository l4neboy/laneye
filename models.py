from flask_sqlalchemy import SQLAlchemy

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