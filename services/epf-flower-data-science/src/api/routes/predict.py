from fastapi import APIRouter
from src.schemas.message import MessageResponse
from src.services.analysis import make_predictions

router = APIRouter()

@router.get("/make_predictions", response_model=MessageResponse)
async def make_prediction_route() -> MessageResponse:
    """Provide predictions for flower classes in the test dataset using the trained model.\n
    Returns a JSON string with the predictions or an error message.
    """
    prediction_message = make_predictions('src/data/Iris.csv')
    return MessageResponse(message=prediction_message)
