from result import Ok, Err, Result
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.engine.cursor import CursorResult
from sqlalchemy.engine.row import Row
from sqlalchemy.sql.expression import delete, func, select, update
from quote import Quote


class Connection:
    def __init__(self):
        self.__engine = create_engine("sqlite:///quotes.db", echo=True)
        self.__meta = MetaData()
        self.__quotes = Table(
            "quote_texts", self.__meta,
            Column("id", Integer, primary_key=True),
            Column("text", String)
        )

    def create_quotes_table(self):
        self.__meta.create_all(self.__engine)

    def insert_quote(self, quote: str) -> int:
        expression = self.__quotes.insert() \
            .values(text=quote)

        with self.__engine.connect() as con:
            result = con.execute(expression)
            new_quote_id = result.inserted_primary_key["id"]

            return new_quote_id

    # Return the ID and the content of one random quote
    def read_random_quote(self) -> Result[Quote, str]:
        expression = select(self.__quotes) \
            .order_by(func.random()) \
            .limit(1)

        result: Row | None
        with self.__engine.connect() as con:
            result = con.execute(expression).fetchone()

        if result is None:
            return Err("No quote could be found. Possibly empty quotes list?")
        else:
            return Ok(Quote(id=result[0], text=result[1]))

    def read_quote(self, id: int) -> Result[Quote, str]:
        expression = select(self.__quotes)\
            .where(self.__quotes.c.id == id)

        result: Row | None
        with self.__engine.connect() as con:
            result = con.execute(expression).fetchone()

        if result is None:
            return Err(f"A quote with id '{id}' could not be found.")
        else:
            return Ok(Quote(id=result[0], text=result[1]))

    def update_quote(self, id: int, text: str) -> Result[None, str]:
        expression = update(self.__quotes) \
            .where(self.__quotes.c.id == id) \
            .values(text=text)

        result: CursorResult
        with self.__engine.connect() as con:
            result = con.execute(expression)

        if result.rowcount == 0:
            return Err(
                f"Could not update quote with id '{id}'. Does it exist?"
            )
        else:
            return Ok(None)

    def delete_quote(self, id: int) -> Result[None, str]:
        expression = delete(self.__quotes) \
            .where(self.__quotes.c.id == id)

        result: CursorResult
        with self.__engine.connect() as con:
            result = con.execute(expression)

        if result.rowcount == 0:
            return Err(
                f"Could not delete quote with id '{id}'. Does it exist?"
            )
        else:
            return Ok(None)
