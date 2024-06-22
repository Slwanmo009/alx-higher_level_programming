#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb

def list_states(username, password, dbname):
    """
    Connects to a MySQL database and lists all states in ascending order by states.id.

    Args:
        username (str): MySQL username
        password (str): MySQL password
        dbname (str): Database name
    """
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname
    )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute the query to retrieve all states sorted by id
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")

    # Fetch all the rows from the executed query
    states = cursor.fetchall()

    # Print the results
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # List all states from the database
    list_states(username, password, dbname)
