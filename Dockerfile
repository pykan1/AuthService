FROM python:3.11

WORKDIR /AuthService

COPY .. .

RUN pip install -r requirements.txt

EXPOSE 8080

WORKDIR /app

CMD ["uvicorn","app.main:app", "--host", "0.0.0.0", "--port", "8000"]