#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument and
lists all cities of the state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys
if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port = 3306, usr = sys.argv[1], passwd = [2], db = sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT cities.name, cities.id FROM 
    cities JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC""", (sys.argv[4]))
    rows = cur.fetchall()
    print(list(row[0] for row in rows), sep=",")

    cur.close()
    db.close()
