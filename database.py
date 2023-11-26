import sqlite3
import threading

db = sqlite3.connect('baza.db', check_same_thread=False)
sql = db.cursor()
lock = threading.Lock()

def create_tables():
    sql.execute("""CREATE TABLE IF NOT EXISTS users (id BIGINT, nick TEXT, cash INT, access INT, bought INT)""")
    sql.execute("""CREATE TABLE IF NOT EXISTS shop (id INT, name TEXT, price INT, tovar TEXT, whobuy TEXT)""")
    db.commit()
