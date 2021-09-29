from flask import Blueprint, render_template, redirect, url_for

api = Blueprint('api', __name__) #check

@api.route('/test')
def test():
    return 'Feel Good Inc.'