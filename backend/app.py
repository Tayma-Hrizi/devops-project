# backend/app.py

import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS # 1. Importation de l'extension CORS

app = Flask(__name__)
CORS(app) # 2. Initialisation de CORS pour toute l'application

# Liste pour stocker les tâches (simule une base de données)
tasks = []
task_id_counter = 1

# Récupérer l'URL du service d'IA depuis les variables d'environnement
AI_SERVICE_URL = os.environ.get("AI_SERVICE_URL", "http://ai_service:8080")

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_counter
    data = request.get_json()
    task_text = data.get('text')

    if not task_text:
        return jsonify({"error": "Task text is required"}), 400

    # 1. Appel au service d'IA pour obtenir la priorité
    try:
        response = requests.post(f"{AI_SERVICE_URL}/predict-priority", json={"task_text": task_text})
        response.raise_for_status() 
        priority = response.json().get('priority', 'NON DÉFINIE')
    except requests.exceptions.RequestException as e:
        print(f"Erreur d'appel AI Service: {e}")
        priority = "ERREUR IA" # Priorité de secours

    # 2. Enregistrement de la tâche (avec la priorité de l'IA)
    new_task = {
        "id": task_id_counter,
        "text": task_text,
        "priority": priority,
        "completed": False
    }
    tasks.append(new_task)
    task_id_counter += 1
    
    return jsonify(new_task), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)