from flask import Blueprint, Flask, render_template, redirect, url_for, jsonify, abort
from flask_restful import Resource, Api

api_bp = Blueprint('api', __name__) #check
api = Api(api_bp)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/api')


