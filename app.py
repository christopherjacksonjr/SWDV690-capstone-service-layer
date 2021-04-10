from flask import Flask, request
from user import SignUp
from flask_restful import Api, Resource
import sqlite3
import shelve

app = Flask(__name__)
api = Api(app)
  
api.add_resource(SignUp, '/signup')

app.run(port=4000,debug=True)