from typing import Optional

from result import Ok, Err, Result
from fastapi import FastAPI
from pydantic import BaseModel
from db import Connection

app = FastAPI()
database = Connection()


class Quote(BaseModel):
    id: Optional[int]
    text: Optional[str]


# Fetch a random inspo quote.
@app.get("/")
def get_random_inspo_quote():
    quote_content = database.read_random_quote()

    match quote_content:
        case Ok(value):
            return {
                **value,
                "status": 200
            }

        case Err(_):
            return {
                "message": "No quote could be found",
                "status": 404
            }


# Get an inspo quote by ID.
@app.get("/q/{id}")
def get_inspo_quote(id: int):
    quote_content = database.read_quote(id)

    match quote_content:
        case Ok(value):
            return {
                **value,
                "status": 200
            }

        case Err(_):
            return {
                "message": f"No quote with id '{id}' could be found",
                "status": 404
            }


# Add an inspo quote
@app.post("/add")
def add_inspo_quote(quote: Quote):
    if quote.text is None:
        return {
            "message": "You must include a 'text' attribute for add quotes.",
            "status": 404
        }
    elif len(quote.text) > 100:
        return {
            "message": "Quote length cannot be more than 100 characters.",
            "status": 404
        }

    new_quote_id = database.insert_quote(quote.text)
    return {
        "id": new_quote_id,
        "status": 200
    }


# Update an inspo quote by ID.
@app.post("/update")
def update_inspo_quote(quote: Quote):
    if quote.id is None:
        return {
            "message":
            "You must include an 'id' attribute for updating quotes.",
            "status": 404
        }

    if quote.text is None:
        return {
            "message":
            "You must include a 'text' attribute for updating quotes.",
            "status": 404
        }

    result = database.update_quote(quote.id, quote.text)

    match result:
        case Ok(_):
            return {"status": 200}

        case Err(_):
            return {
                "message":
                f"Could not update quote with id '{quote.id}'. Does it exist?",
                "status": 404
            }


# Delete an inspo quote by ID.
@app.post("/delete")
def delete_inspo_quote(quote: Quote):
    if quote.id is None:
        return {
            "message":
            "You must include an 'id' attribute for updating quotes.",
            "status": 404
        }

    result = database.delete_quote(quote.id)

    match result:
        case Ok(_):
            return {"status": 200}

        case Err(_):
            return {
                "message":
                f"Could not delete quote with id '{id}'. Does it exist?",
                "status": 404
            }
