# ai_service/ai_api.py

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Modèle pour la donnée entrante (le texte de la tâche)
class TaskIn(BaseModel):
    task_text: str

# Modèle pour la donnée sortante (la priorité prédite)
class PredictionOut(BaseModel):
    priority: str

def simple_prioritizer(text: str) -> str:
    """
    Logique d'IA simulée : 
    - Si le texte contient 'urgent' ou 'maintenant', c'est 'HAUTE'.
    - Sinon, c'est 'MOYENNE'.
    """
    if "urgent" in text.lower() or "maintenant" in text.lower():
        return "HAUTE"
    return "MOYENNE"

@app.post("/predict-priority", response_model=PredictionOut)
def predict_priority(task: TaskIn):
    """Point de terminaison pour prioriser la tâche."""
    priority = simple_prioritizer(task.task_text)
    return {"priority": priority}

@app.get("/")
def health_check():
    return {"status": "AI Service Running"}