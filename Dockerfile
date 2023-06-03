FROM python:3.11

WORKDIR /AuthService

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR app

CMD ["uvicorn","main:app", "--host", "0.0.0.0", "--port", "8000"]