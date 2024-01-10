import json
from sklearn.model_selection import train_test_split
from src.services.cleaning import procesing_datast
import pandas as pd
from typing import Tuple
import os

def divide_data(file_location: str, test_ratio=0.2) -> Tuple[str, str]:
    """Divide the dataset into training and testing sets.

    Args:
        file_location (str): Path to the dataset file.
        test_ratio (float, optional): Proportion of the dataset to include in the test split (default is 0.2, or 20%).

    Returns:
        Tuple[str, str]: A tuple containing the training and testing datasets in JSON format, or an error message.
    """
    try:
        if not os.path.isfile(file_location):
            return ("Dataset file not found", "")
        dataset_json = procesing_datast(file_location)
        dataset = pd.DataFrame(json.loads(dataset_json))
        train_set, test_set = train_test_split(
            dataset, test_size=test_ratio, random_state=42, stratify=dataset['Species'])
        return train_set.to_json(orient='records'), test_set.to_json(orient='records')
    except Exception as error:
        print(f"Error encountered: {error}")
        return ("Error occurred in data division", "")
