from fastapi import APIRouter
from src.schemas.message import MessageResponse
from src.services.analysis import train_knn_model

router = APIRouter()

@router.post("/initiate_training", response_model=MessageResponse)
async def initiate_training_route() -> MessageResponse:
    """Initiate training of the model using specified parameters and dataset, and save it in the models directory.\n
    Returns a message indicating the outcome of the training or an error message.
    """
    training_message = train_knn_model('src/data/Iris.csv')
    return MessageResponse(message=training_message)
