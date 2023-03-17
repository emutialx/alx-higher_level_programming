#!/usr/bin/python3
"""
displays all values in the states table of hbtn_0e_0_usa where name matches the argument
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], database=argv[3], host="localhost", port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY id ASC".format(argv[4]))
    states = cur.fetchall()
    for state in states:
        print(state)
