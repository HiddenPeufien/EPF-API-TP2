from sklearn.neighbors import KNeighborsClassifier
from src.services.utils import divide_data
from src.services.parameters import load_configurations
import pandas as pd
import joblib
import json
import os

def train_knn_model(dataset_path: str) -> str:
    """
    Train a KNN classification model with provided parameters and save it using joblib.
    Args:
        dataset_path (str): Path to the dataset file.
    Returns:
        str: Status message about the training outcome or an error message.
    """
    try:
        model_params = json.loads(load_configurations(
            'src\config\model_config.json'))
        training_data, _ = divide_data(dataset_path)
        training_df = pd.DataFrame(json.loads(training_data))
        features = training_df.drop('Species', axis=1)
        labels = training_df['Species']
        knn_classifier = KNeighborsClassifier(**model_params)
        knn_classifier.fit(features, labels)
        joblib.dump(knn_classifier, 'src/models/knn_classifier.joblib')
        return ("KNN model successfully trained and saved")
    except Exception as error:
        print(f"Training error: {error}")
        return ("Error in model training process")

def make_predictions(model_file_path: str) -> str:
    """
    Generate predictions using a trained KNN model on test data.

    Args:
        model_file_path (str): Path to the dataset for prediction.

    Returns:
        str: JSON formatted string of predictions or an error message.
    """
    try :
        if not os.path.exists(model_file_path):
            return ("Dataset file not found")
        if not os.path.exists('src/models/knn_classifier.joblib'):
            train_knn_model(model_file_path)
        _, test_data = divide_data(model_file_path)
        knn_model = joblib.load('src/models/knn_classifier.joblib')
        test_df = pd.DataFrame(json.loads(test_data))
        features_test = test_df.drop('Species', axis=1)
        predictions = knn_model.predict(features_test)
        return json.dumps(predictions.tolist())
    except Exception as prediction_error :
        print(f"Prediction error: {prediction_error}")
        return ("Error during prediction process")
    
