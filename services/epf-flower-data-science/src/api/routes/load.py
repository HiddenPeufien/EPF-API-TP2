from fastapi import APIRouter
from src.schemas.message import MessageResponse
from src.services.data import read_dataset_to_json
router = APIRouter()

@router.get("/retrieve", response_model=MessageResponse)
async def retrieve_dataset_route() -> MessageResponse:
    """Retrieve the Iris dataset from a CSV file and format it as JSON.\n
    Returns a Message containing the dataset or an error message.
    """
    dataset_message = read_dataset_to_json('src/data/Iris.csv')
    return MessageResponse(message=dataset_message)
