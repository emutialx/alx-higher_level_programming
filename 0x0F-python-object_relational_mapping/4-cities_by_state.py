#!/usr/bin/python3
"""
This script lists all cities from
the database `hbtn_0e_4_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Access to the database and get the cities
    from the database.
    """

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], database=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities, states WHERE cities.state_id = states.id ORDER BY cities.id ASC")
    cities = cur.fetchall()
    for city in cities:
        print(city)
