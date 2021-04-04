import sqlite3 as lit

def main():
    try:
        db = lit.connect('vacationHub.db')
        print("Database created.", db)
    except:
        print("Failed to create database.")
        
main()