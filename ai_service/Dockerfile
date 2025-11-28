# ai_service/Dockerfile
# Image de base Python pour l'IA
FROM python:3.10-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les dépendances et les installer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code de l'API
COPY ai_api.py .

# Le conteneur écoute sur le port 8080
EXPOSE 8080

# Commande pour lancer l'API avec Uvicorn
CMD ["uvicorn", "ai_api:app", "--host", "0.0.0.0", "--port", "8080"]