from .Model import Model
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String,text

class model(Model):
    def __init__(self):
        self.engine = create_engine("sqlite+pysqlite:///entries.db", echo=True, future = True)
        metadata = MetaData(self.engine)
        Table("flags", metadata,
                Column('x', Integer),
                Column('y', Integer),
                Column('message', String)
        )
        metadata.create_all()

    def select(self):
        """
        Gets all rows from the database
        Each row contains: x, y, message
        :return: List of lists containing all rows of database
        """
        with self.engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM flags"))
            return result.all()

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
        with self.engine.begin() as conn:
            conn.execute(text("INSERT INTO flags (x, y, message) VALUES (:x, :y, :message)"), params)

        return True
