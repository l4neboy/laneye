from flask import Blueprint, render_template, redirect, url_for

main = Blueprint('main', __name__, template_folder='templates') #check

@main.route('/newmain')
def newmain():
    return render_template('main/index.html')

@main.route('/aboutme')
def aboutme():
    return render_template('main/aboutme.html')


