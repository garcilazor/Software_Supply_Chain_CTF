from .Model import Model
import sqlite3
DB_FILE = 'entries.db'    # file for our Database

class model(Model):
    def __init__(self):
        # Make sure our database exists
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("select count(rowid) from flags")
        except sqlite3.OperationalError:
            cursor.execute("create table flags (x integer, y integer, message text)")
        cursor.close()

    def select(self):
        """
        Gets all rows from the database
        Each row contains: x, y, message
        :return: List of lists containing all rows of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM flags")
        return cursor.fetchall()

    def insert(self, x, y, message):
        """
        Inserts entry into database
        :param x: Int
        :param y: Int
        :param message: String
        :return: True
        :raises: Database errors on connection and insertion
        """
        params = {'x':x, 'y':y, 'message':message}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into flags (x, y, message) VALUES (:x, :y, :message)", params)

        connection.commit()
        cursor.close()
        return True
