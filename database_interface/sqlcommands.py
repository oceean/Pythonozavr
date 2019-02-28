CREATE_TABLE = """CREATE TABLE {table} (
  {columns}
);"""

DROP_TABLE = "DROP TABLE IF EXISTS {table}"

FIND = """SELECT {selection}
FROM {table}
WHERE {conditions};"""

GET = """SELECT {selection}
FROM {table};
"""

INSERT = """INSERT INTO {table} ({columns})
VALUES ({values});"""

UPDATE = """UPDATE {table}
SET {updates}
WHERE id={id};"""