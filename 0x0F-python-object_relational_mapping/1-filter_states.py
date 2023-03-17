#!/usr/bin/python3
"""
Lists all states with a name starting with N from the database hbtn_0e_0_usa.
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    con = MySQLdb.connect(host="localhost", port=3306, user=argv[1], password=argv[2], database=argv[3])
    cur = con.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '%N' ORDER BY id ASC")
    db = cur.fetchall()
    for i in db:
        print(i)
