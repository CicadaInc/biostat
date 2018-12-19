import sqlite3


def connect():
    """ Connect to MySQL database """
    try:
        conn = sqlite3.connect("products.db")  # или :memory: чтобы сохранить в RAM

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products2")

        row = cursor.fetchall()

        print(row)

        # for row in cursor:
        #     print(row)


    except Exception as e:
        print(e)

    finally:
        conn.close()


if __name__ == '__main__':
    connect()
