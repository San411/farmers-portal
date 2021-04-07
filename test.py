import sqlite3

conn = sqlite3.connect('user.db')
c = conn.cursor()
c.execute("DELETE FROM user")
conn.commit()
conn.close()