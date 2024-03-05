FROM python:3.7

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY calculator /app/calculator

CMD ["python", "-m", "calculator.app"]

