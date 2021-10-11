from flask import Blueprint, Flask, render_template, redirect, url_for, jsonify, abort
from flask_restful import Resource, Api

api = Blueprint('api', __name__) #check

apix = Api(api)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

apix.add_resource(HelloWorld, '/api')


