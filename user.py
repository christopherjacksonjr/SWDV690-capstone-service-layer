import sqlite3
from flask_restful import Resource
from flask import request

# class User:
#     def __init__(self, userId, username, password, firstName, lastName, emailAddress, phoneNumber, location):
#         self.userId = userId
#         self.username = username
#         self.password = password
#         self.firstName = firstName
#         self.lastName = lastName
#         self.emailAddress = emailAddress
#         self.phoneNumber = phoneNumber
#         self.location = location
#         
#     @classmethod
#     def get(clss, username):
#         data = request.get_json(username)
#         
#         conn = sqlite3.connect('vacationHub.db')
#         cursor = conn.cursor()
#         
#         q1 = "SELECT * FROM user WHERE username=?"
#         result = cursor.execute(q1,(username,))
#         row = result.fetchone()
#         if row:
#             user = clss(*row)
#         else:
#             user = None
#         return user
        
#     def findByUsername(self, username):
#         conn = sqlite3.connect('vacationHub.db')
#         cursor = conn.cursor()
#         
#         q1 = "SELECT * FROM user WHERE username = ?"
#         result = cursor.execute(q1, (username,))
#         row = result.fetchone()
#         
#         if row:
#             user = User(*row)
#         else:
#             user = None
#             
#         return user
#     
#     def findByUserId(self, userId):
#         conn = sqlite3.connect('vacationHub.db')
#         cursor = conn.cursor()
#         
#         q1 = "SELECT * FROM user WHERE userId = ?"
#         result = cursor.execute(q1, (userId,))
#         row = result.fetchone()
#         
#         if row:
#             user = User(*row)
#         else:
#             user = None
#             
#         return user
        
class SignUp(Resource):
    def post(self):
        data = request.get_json()
        
        conn = sqlite3.connect('vacationHub.db')
        cursor = conn.cursor()
        
        q1 = "CREATE TABLE IF NOT EXISTS user (userId INTEGER PRIMARY KEY, username TEXT, password TEXT, firstName TEXT, lastName TEXT, emailAddress TEXT, phoneNumber TEXT, location TEXT)"
        cursor.execute(q1)
        q2 = "INSERT INTO user VALUES(NULL, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(q2, (data['username'], data['password'], data['firstName'], data['lastName'], data['emailAddress'], data['phoneNumber'], data['location']))
        
        conn.commit()
        conn.close()
        
        return {"message": "User successfully created."}