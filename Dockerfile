FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code

RUN rm /code/quotes.db

RUN python3 /code/init_db.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
