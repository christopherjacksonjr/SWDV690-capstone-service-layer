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
        db = g._database = shelve.open("../post.db")
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
        
class PostList(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())
        
        posts = []
        
        for key in keys:
            posts.append(shelf[key])
            
        return {'message': 'Success', 'data': posts}, 200
    
    def post(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument('post_id', required=True)
        parser.add_argument('username', required=True)
        parser.add_argument('likes', required=True)
        parser.add_argument('comments', required=True)
        parser.add_argument('saves', required=True)
        parser.add_argument('travel_expense', required=True)
        parser.add_argument('lodging_expense', required=True)
        parser.add_argument('rating', required=True)
        parser.add_argument('review', required=True)
        
        args = parser.parse_args()
        
        shelf = get_db()
        shelf[args['post_id']] = args
        
        return {'message': 'Post created.', 'data': args}, 201
    
class Post(Resource):
    def get(self, post_id):
        shelf = get_db()
        
        if not(post_id in shelf):
            return {'message': 'Post not found', 'data': {}}, 404
        
        return {'message': 'Post found', 'data': shelf[post_id]}, 200
    
    def delete(self, post_id):
        shelf = get_db()
        
        if not(post_id in shelf):
            return {'message': 'Post not found', 'data': {}}, 404
        
        del shelf[post_id]
        return '', 204
        
api.add_resource(UserList, '/post')
api.add_resource(User, '/post/<string:post_id>')