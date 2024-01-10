from fastapi import APIRouter
from src.schemas.message import MessageResponse
from src.services.cleaning import procesing_datast
router = APIRouter()

@router.get("/process_data", response_model=MessageResponse)
async def process_data_route() -> MessageResponse:
    """Refine The Iris Dataset by eliminating the Id and modifying the Species column.\n
    Returns the refined dataset in JSON format or an error message.
    """
    processed_message = procesing_datast('src/data/Iris.csv')
    return MessageResponse(message=processed_message)
