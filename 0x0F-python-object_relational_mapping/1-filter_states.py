#!/usr/bin/python3
"""[summary]
    """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],)
    cur = db.cursor()
    # HERE I have to know SQL to grab all states in my database
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%'ORDER BY states.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
