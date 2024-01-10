from src.services.data import read_dataset_to_json
import pandas as pd
import json
import os


def procesing_datast(file_path: str) -> str:
    """ Process the dataset to be used in the analysis,
    dropping the Id column and replacing the Iris- prefix in the Species column.

    Args:
        file_path (str): Path to the dataset.

    Returns:
        str: JSON string with the processed dataset or an error message.
    """
    try:
        if not os.path.exists(file_path):
            return ("The dataset was not found")
        json_data = read_dataset_to_json(file_path)
        data = pd.DataFrame(json.loads(json_data))
        data.drop('Id', axis=1, inplace=True)
        data["Species"] = data['Species'].str.replace('Iris-', '')
        return data.to_json(orient='records')
    except Exception as e:
        print(f"An error occurred: {e}")
        return ("An error occurred during the dataset processing")
