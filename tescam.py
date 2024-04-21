from pysql import MY_DB
import sqlite3
conn  = sqlite3.connect("data.db")

c = conn.cursor()
c.execute("ALTER TABLE consumer_goods ADD column amount INTEGER DEFAULT 0")
conn.commit()
conn.close()