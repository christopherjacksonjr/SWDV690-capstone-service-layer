#Import statements.
from flask import Flask
from flask import g
import markdown
import os
import shelve
from flask_restful import Resource, Api, reqparse

#Create an instnace of Flask.
app = Flask(__name__)

# Create the API
api = Api(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("../user.db")
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    #Open index file.
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:
        
        #Read the content of the file.
        content = markdown_file.read()
        
        #Convert to HTML
        return markdown.markdown(content)
    
class UserList(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())
        
        users = []
        
        for key in keys:
            users.append(shelf[key])
            
        return {'message': 'Success', 'data': users}, 200
    
    def post(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument('username', required=True)
        parser.add_argument('first_name', required=True)
        parser.add_argument('last_name', required=True)
        parser.add_argument('email_address', required=True)
        parser.add_argument('phone_number', required=True)
        parser.add_argument('location', required=True)
        
        args = parser.parse_args()
        
        shelf = get_db()
        shelf[args['username']] = args
        
        return {'message': 'User created.', 'data': args}, 201
    
class User(Resource):
    def get(self, user_name):
        shelf = get_db()
        
        if not(user_name in shelf):
            return {'message': 'User not found', 'data': {}}, 404
        
        return {'message': 'User found', 'data': shelf[user_name]}, 200
    
    def delete(self, user_name):
        shelf = get_db()
        
        if not(user_name in shelf):
            return {'message': 'User not found', 'data': {}}, 404
        
        del shelf[user_name]
        return '', 204
        
api.add_resource(UserList, '/user')
api.add_resource(User, '/user/<string:user_name>')