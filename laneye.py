from flask import Flask, render_template, request, redirect
#from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Item, User
from auth.auth import auth #import auth
from main.main import main #import main
from flask_login import LoginManager



app = Flask(__name__)
app.config.from_pyfile('config.py')
#db = SQLAlchemy(app)
migrate = Migrate(app, db)
db.init_app(app) #initialising db here
app.register_blueprint(auth) # blueprint for auth routes
app.register_blueprint(main) # blueprint for new main routes

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))

'''@app.route("/misterything")
def index():
    items = Item.query.order_by(Item.price).all()
    return render_template('index.html', data=items)'''

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

