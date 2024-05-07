import sqlite3

from pysql import MY_DB

my_db = MY_DB()
my_db.connect('data.db')
my_db.update_amount("consumer_goods",{"id":1})
my_db.close()