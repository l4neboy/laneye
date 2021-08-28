from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_pyfile('config.py')
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://laneps:laneps@128.199.52.144:5432/laneps"
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#провеОчка

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


@app.route("/")
def index():
    items = Item.query.order_by(Item.price).all()
    return render_template('index.html', data=items)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        item = Item(title=title, price=price)
        try:
            db.session.add(item)
            db.session.commit()
            return render_template('index.html') #тут
        except:
            return 'Запись не добавлена'
    else:
        return render_template('create.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

