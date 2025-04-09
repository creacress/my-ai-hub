FROM python:3.13-slim


# Dossier de travail
WORKDIR /app

# Copie du code API
COPY . .

# Installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Démarrage FastAPI avec Uvicorn (4 workers, event loop optimisée)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4", "--loop", "uvloop", "--http", "httptools"]
