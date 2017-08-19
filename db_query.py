import sqlite3
from datetime import datetime

conn = sqlite3.connect('cafedb.db')

dateStart = datetime.strptime('Aug 19 2017  5:00PM', '%b %d %Y %I:%M%p')
dateEnd = datetime.strptime('Aug 19 2017  5:08PM', '%b %d %Y %I:%M%p')

c = conn.cursor()

#c.execute('SELECT * FROM bills') # WHERE symbol=?', t)


c.execute('SELECT * FROM bills WHERE endingTime BETWEEN ? AND ?', (dateStart, dateEnd))

print(c.fetchall())
