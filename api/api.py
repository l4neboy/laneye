from flask import Blueprint, Flask, request, render_template, redirect, url_for, jsonify, abort
from flask_restful import Resource, Api
from models import db, BookModel

api_bp = Blueprint('api', __name__) #check
api = Api(api_bp)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class BooksList(Resource):
    def get(self):
        books = BookModel.query.all()
        return {'Books': list(x.json() for x in books)}

    def post(self):
        data = request.get_json()
        new_book = BookModel(data['name'], data['price'], data['author'])
        db.session.add(new_book)
        db.session.commit()
        return new_book.json(), 201


api.add_resource(HelloWorld, '/api')
api.add_resource(BooksList, '/books')

