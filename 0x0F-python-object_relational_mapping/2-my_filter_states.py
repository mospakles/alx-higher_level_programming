#!/usr/bin/python3
"""
Lists all values in the states tables of a database where name
matches the argument
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
            db=sys.argv[3], port=3306)
