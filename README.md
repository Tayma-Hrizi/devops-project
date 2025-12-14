#  ToDo IA App

Application ToDo intelligente avec priorisation automatique des tâches via IA.

# Fonctionnalités
- Ajouter des tâches
- Priorité automatique (HAUTE, MOYENNE, BASSE)
- Architecture microservices
- Déploiement Docker

# Technologies
- Frontend : HTML, CSS, Bootstrap, Nginx
- Backend : Python, Flask
- IA : FastAPI, Python
- Docker & Docker Compose
- Vagrant
- Jenkins

# Structure du projet
todo-ia-app/
│── frontend/
│   ├── Dockerfile
│   └── index.html
│
│── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
│── ai_service/
│   ├── ai_api.py
│   ├── requirements.txt
│   └── Dockerfile
│
│── docker-compose.yml
│── README.md


# Lancement
```bash
docker-compose up --build

