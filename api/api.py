from flask import Blueprint, render_template, redirect, url_for

main = Blueprint('api', __name__, template_folder='templates') #check

@api.route('/test')
def test():
    return 'Feel Good Inc.'