import sqlite3
db_name = 'customer.db'
"""
Pending CRUD operation functions
Database choices: mongodb, mysql?
Data isn't sequenced

Image storing options: store in databse, store in separate server, store in cloud and use url (maybe abuse discord lmao?...)
"""
# conn = sqlite3.connect(db_name)

# c = conn.cursor()

# c.execute("""
#     CREATE TABLE customers (
#         name text,
#         phone_number integer,
#         location text
#     )
# """)

# c.execute("""
#     INSERT INTO customers VALUES (
#         'Mohammed',
#         '0502934123',
#         'al warsan'
#     )
# """)

# customers_list = [
#     ('Ahmed', '3124321421', 'gulf'),
#     ('Rashid', '3783421', 'jumeirah'),
#     ('Hassan', '23914241', 'motor city')
# ]

# c.executemany("INSERT INTO customers VALUES (?,?,?)", customers_list)

# c.execute("SELECT * FROM customers")

# # c.fetchone()
# # c.fetchmany(2)

# print(c.fetchall())

# conn.commit()

# conn.close()

def createOrder(cursor, customer):
    """
    customer: tuple (name, phone, location)
    """
    cursor.execute(
        f"INSERT INTO customers VALUES ({customer[0]}, {customer[1]}, {customer[2]})"
    )


def readOrder(cursor):
    """
    """
    return cursor.fetchone()


def updateOrder():
    pass


def deleteOrder():
    pass


def main():
    conn = sqlite3.connect(db_name)
    #command parser to parse database operations


if __name__ == "__main__":
    main()