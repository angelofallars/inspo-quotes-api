# 🎆 Inspo Quotes API

An API for inspirational quotes, built with FastAPI and SQLAlchemy.

With this API, you can fetch quotes, add them, update them and delete them.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

## 🐳 Setup and Run (Docker)

`sudo docker build -t inspo_quotes_api ./`

`sudo docker run -p 80:80 inspo_quotes_api`

## 🔨 Setup (Manual)

This program requires Python 3.10.

### Init

```bash
python3 -m venv venv

source ./venv/bin/activate
pip install -r requirements.txt
python3 init_db.py
```

### Running

To run this in a dev environment:

```bash
source ./venv/bin/activate
uvicorn main:app --reload
```

## API response format

The default response format for all the `GET` requests is plain text, but you can provide another HTTP `Accept` header to modify the response format.

Available `Accept` headers:
- `text/plain` - Plain text response (default)
- `application/json` - JSON response

## ➡️ API endpoints

### `GET /`

Fetch a random inspirational quote.

```bash
$ curl 127.0.0.1:8000/

{
  "id": 3,
  "quote": "I have not failed. I've just found 10,000 ways that won't work.",
  "status": 200
}
```

### `GET /q/<quote_id>`

Fetch a specific quote.

```bash
$ curl 127.0.0.1:8000/q/5

{
    "id": 5,
    "quote": "Everything you can imagine is real.",
    "status": 200
}
```

### `POST /add`

Add a new quote. You will get the ID of the quote through the JSON response. The max quote length is 100 characters.

```bash
$ curl 127.0.0.1:8000/add -X POST -H "Content-Type: application/json" -d '{ "text": "You miss all the shots you don'\''t take." }'

{
    "id": 10,
    "status": 200
}
```

### `POST /update`

Update a quote by ID with new text.

```bash
$ curl 127.0.0.1:8000/update -X POST -H "Content-Type: application/json" -d '{ "id": 6, "text": "When you have a dream, you'\''ve got to grab it and never let go." }'

{
    "status": 200
}
```

### `POST /delete`

Delete a quote by ID.

```bash
$ curl -X POST 127.0.0.1:8000/delete -H "Content-Type: application/json" -d '{ "id": 7 }'

{
    "status": 200
}
```

## 📄 License

This program is licensed under the MIT license.
