from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import Item

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#провеОчкаgit
#121212

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

