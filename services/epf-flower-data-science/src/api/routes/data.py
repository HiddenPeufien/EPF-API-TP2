from fastapi import APIRouter
from src.schemas.message import MessageResponse
from src.services.data import fetch_and_save_dataset
router = APIRouter()

@router.post("/fetch_dataset")
def fetch_dataset_data() -> MessageResponse:
    """ Fetch the Iris dataset from UCI Machine Learning Repository and store it in the data directory.
    Returns a message indicating the outcome of the operation.
    """

    operation_status = fetch_and_save_dataset("src/data", "uciml/iris")
    response_message = "Dataset successfully fetched" if operation_status else "Failed to fetch dataset"
    return MessageResponse(message=response_message)
