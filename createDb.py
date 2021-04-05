import sqlite3 as lit

def main():
    try:
        db = lit.connect('user.db')
        print("Database created.", db)
    except:
        print("Failed to create user database.")
        
    try:
        db = lit.connect('post.db')
        print("Database created.", db)
    except:
        print("Failed to create post database.")
        
main()