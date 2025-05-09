
import json
from models import User, db  # Importa `User` correctamente

JSON_FILE = "users.json"

def load_users():
    try:
        with open(JSON_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_users(users):
    with open(JSON_FILE, "w") as file:
        json.dump(users, file, indent=4)

