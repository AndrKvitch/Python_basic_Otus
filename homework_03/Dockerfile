FROM python:3.9-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install poetry "poetry==1.4.2"
RUN poetry config virtualenvs.create false --local
COPY pyproject.toml poetry.lock ./
RUN poetry install --only view
COPY . .

CMD ["uvicorn", "view:app", "--host 0.0.0.0", "--port 8000"]

EXPOSE 8000