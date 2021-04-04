import sqlite3 as lit

def main():
    try:
        db = lit.connect('vacationHub.db')
        cur = db.cursor()
        
        userTableQuery = "CREATE TABLE user (UserId INT, UserName TEXT, FirstName TEXT, LastName TEXT, email TEXT, Phone INT, Location TEXT, PRIMARY KEY(UserId))"
        postTableQuery = "CREATE TABLE post (PostId INT, UserId INT, Likes INT, Comments INT, Saves INT, TravelExpense INT, LodgingExpense INT, Rating INT, Review TEXT, PRIMARY KEY(PostId), FOREIGN KEY(UserId) REFERENCES User(UserId))"
#         groupTableQuery = "CREATE TABLE group (GroupId INT, Members INT, PRIMARY KEY(GroupId))"

        cur.execute(userTableQuery)
        cur.execute(postTableQuery)
#         cur.execute(groupTableQuery)
        print("Tables created.")
        
    except lit.Error as e:
        print("Unable to create tables.")
main()