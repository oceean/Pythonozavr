import psycopg2
from . import sqlcommands


class DataBaseException(Exception):
    """ PostgreSQL database class exceptions
    """
    pass
class DataCoderException(Exception):
    """ PostgreSQL database class exceptions
    """
    pass


class DataBase:
    """ PostgreSQL database class
    """

    def __init__(self, host:str='localhost', user:str="postgres", password:str="test"):
        """
            >>> testdb = DataBase()
            >>> type(testdb) == DataBase
            True
        """
        try:
            # Connect to database
            dbident = "user='{0}' host='{1}' password='{2}'".format(user, host, password)
            self.connection = psycopg2.connect(dbident)
        except psycopg2.OperationalError:
            # Exception if Docker has not setuped
            raise DataBaseException("Cant setup connection %s."
            "Please check Postgres Docker container" % dbident)
        pass

    def execute(self, command:str) -> list:
        """
            >>> testdb = DataBase()
            >>> type(testdb.execute('SELECT * FROM pg_database'))
            <class 'list'>
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(command)
            results = []
            try:
                results = cursor.fetchall()
            except:
                self.connection.commit()
            cursor.close()
            return results
        except psycopg2.InternalError:
            self.connection.rollback()
            self.execute(command)
        except psycopg2.ProgrammingError:
            raise DataCoderException("Can't done:\n\n%s\n" % command)


class Table(DataBase):
    def __init__(self, table_name, columns=["name TEXT"], host="localhost"):
        super().__init__(host=host, password="mbmbase")
        self.table_name = table_name
        self.columns = columns

    def _with_columns(self, values):
        sc = [
            "id SERIAL PRIMARY KEY",
            *self.columns,
            "created TIMESTAMP",
            "updated TIMESTAMP",
        ]
        ols = []
        for value in values:
            ol = {}
            for i, c in enumerate(sc):
                ol[c.split(" ")[0]] = value[i]
            ols.append(ol)
        return ols


    def create(self):
        self.execute(sqlcommands.CREATE_TABLE.format(
            table = self.table_name,
            columns = ",\n  ".join([
                "id SERIAL PRIMARY KEY",
                *self.columns,
                "created TIMESTAMP",
                "updated TIMESTAMP",
            ])
        ))

    def drop(self):
        self.execute(sqlcommands.DROP_TABLE.format(
            table = self.table_name
        ))

    def select(self, selection="*"):
        sel = self.execute(sqlcommands.GET.format(
            table = self.table_name,
            selection = selection
        ))
        return self._with_columns(sel)

    def find(self, **where):
        conditions = []
        for key, value in where.items():
            if type(value) == str:
                value = "'{}'".format(value)
            conditions.append("{}={}".format(key, value))
        sel = self.execute(sqlcommands.FIND.format(
            table = self.table_name,
            selection = "*",
            conditions = "\n  AND ".join(conditions)
        ))
        return self._with_columns(sel)

    def insert(self, **columns_with_values):
        columns = ["created", "updated"]
        for c in columns_with_values.keys():
            columns.append(str(c))
        values = ["now()", "now()"]
        for v in columns_with_values.values():
            if type(v) == str:
                values.append("'{}'".format(v))
            else:
                values.append(str(v))
        self.execute(sqlcommands.INSERT.format(
            table = self.table_name,
            columns = ", ".join(columns),
            values = ", ".join(values)
        ))

    def update(self, iid, **columns_with_values):
        conditions = ["updated=now()"]
        for key, value in columns_with_values.items():
            conditions.append("{}='{}'".format(key, value))
        self.execute(sqlcommands.UPDATE.format(
            table = self.table_name,
            updates = ",".join(conditions),
            id = iid
        ))
