from flask import Blueprint, render_template, redirect, url_for

main = Blueprint('main', __name__, template_folder='templates') #check

@main.route('/test')
def test():
    return 'Feel good inc'


