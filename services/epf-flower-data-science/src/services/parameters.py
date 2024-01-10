import json
import os
from src.services.firestore import FirestoreClient

def load_configurations(json_file_path: str) -> str:
    """Load settings from a JSON file and return them as a JSON string.

    Args:
        json_file_path (str): Path to the JSON settings file.

    Returns:
        str: JSON string of the settings or an error message.
    """
    try:
        if not os.path.exists(json_file_path):
            return ("Settings file is missing")
        with open(json_file_path, 'r') as file:
            config_data = json.load(file)
        return json.dumps(config_data)
    except Exception as error:
        print(f"An error occurred: {error}")
        return ("An issue occurred while loading settings")

def load_config_from_firestore(db_collection: str, doc_key: str) -> None:
    try:
        db_client = FirestoreClient()
        return json.dumps(db_client.get(db_collection, doc_key))
    except Exception as error:
        print(f"An error occurred: {error}")
        return ("An issue occurred while fetching settings from Firestore")
