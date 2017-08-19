import sqlite3
from datetime import datetime, timedelta

conn = sqlite3.connect('cafedb.db')

# dateStart = datetime.strptime('Aug 19 2017  5:00PM', '%b %d %Y %I:%M%p')
# dateEnd = datetime.strptime('Aug 19 2017  5:08PM', '%b %d %Y %I:%M%p')

c = conn.cursor()

#c.execute('SELECT * FROM bills') # WHERE symbol=?', t)


# c.execute('SELECT * FROM bills WHERE endingTime BETWEEN ? AND ?', (dateStart, dateEnd))

def get_docs():
    c.execute('SELECT * FROM bills')
    return c.fetchall()

def get_daily_docs():
    c.execute('SELECT * FROM bills WHERE endingTime BETWEEN ? AND ?', (datetime.now() - timedelta(hours=17), datetime.now()))
    return c.fetchall()