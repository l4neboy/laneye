from flask import Blueprint, render_template
from models import db

auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/login')
def login():
    return render_template('auth/login.html')

@auth.route('/signup')
def signup():
    return render_template('auth/signup.html')

@auth.route('/logout')
def logout():
    return 'Logout'

@auth.route('/profile')
def profile():
    return render_template('auth/profile.html')