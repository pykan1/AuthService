FROM python:3.10

WORKDIR /AuthService

COPY .. .

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["uvicorn","app.main:app", "--host", "0.0.0.0", "--port", "8000"]