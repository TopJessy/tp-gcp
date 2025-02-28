# Utilisation de l'image officielle Python 3.9 comme base
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier tous les fichiers du répertoire local vers le conteneur
COPY . /app

# Installer les dépendances à partir du fichier requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port 8080 pour l'application Flask
EXPOSE 8080

# Commande pour démarrer l'application
CMD ["python", "app_bucket.py"]
