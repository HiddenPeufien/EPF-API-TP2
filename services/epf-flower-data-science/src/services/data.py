from kaggle.api.kaggle_api_extended import KaggleApi
from requests.exceptions import HTTPError
import pandas as pd
import os

def fetch_and_save_dataset(storage_directory: str, kaggle_dataset_url: str) -> bool:
    """
    Retrieve and decompress a dataset from Kaggle.

    Args:
        storage_directory (str): Path to store the dataset.
        kaggle_dataset_url (str): URL of the Kaggle dataset, including username and dataset name.

    Returns:
        bool: True if the operation is successful, False otherwise.
    """
    try:
        print(f"Fetching dataset from {kaggle_dataset_url} to {storage_directory}")
        kaggle_client = KaggleApi()
        kaggle_client.authenticate()
        kaggle_client.dataset_download_files(
            dataset=kaggle_dataset_url, path=storage_directory, unzip=True)
        return True
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err.response.status_code}")
    except Exception as general_err:
        print(f"Error during download: {general_err}")

    return False

def read_dataset_to_json(dataset_file_path: str) -> str:
    """Read a dataset from a CSV file and convert it to JSON.

    Args:
        dataset_file_path (str): File path of the dataset.

    Returns:
        str: JSON string of the dataset or an error message.
    """
    try:
        if not os.path.isfile(dataset_file_path):
            return ("Dataset file not found")
        dataset = pd.read_csv(dataset_file_path)
        return dataset.to_json(orient='records')
    except Exception as load_err:
        print(f"Error reading dataset: {load_err}")
        return ("Error while converting dataset to JSON")
