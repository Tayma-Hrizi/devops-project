# backend/Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

# Le Backend doit connaître l'URL du service d'IA
# Cette variable sera remplie par docker-compose.yml
CMD ["python", "app.py"]