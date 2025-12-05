import os
import json


DATA_FILE = "User.json"

def load_data():

    if not os.path.exists(DATA_FILE):
        return {}
    
    try:
        with open(DATA_FILE, encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        print("Cannot load data file.")
        return {}

def save_data(data):

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)    

