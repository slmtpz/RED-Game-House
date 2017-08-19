import sqlite3


def init():
    global conn
    conn = sqlite3.connect('cafedb.db')


def saveBill(bill):
    c = conn.cursor()

    for game in bill.games:
        product = game[0]['name']+' / ' + str(game[1])
        c.execute("INSERT INTO bills VALUES (?, ?, 'game', ?, ?, ?)", (bill.startingTime, bill.endingTime, product, game[2], game[3]))

    for extra in bill.extras:
        c.execute("INSERT INTO bills VALUES (?, ?, 'extra', ?, ?, ?)", (bill.startingTime, bill.endingTime, extra['name'], 1, extra['charge']))

    for other in bill.others:
        c.execute("INSERT INTO bills VALUES (?, ?, 'other', ?, ?, ?)", (bill.startingTime, bill.endingTime, other[0], 1, other[1]))

    conn.commit()


def createTables():
    c = conn.cursor()

    c.execute('''CREATE TABLE bills
                    (startingTime text, endingTime text, type text, product real, quantity real, price real)''')

    conn.commit()
