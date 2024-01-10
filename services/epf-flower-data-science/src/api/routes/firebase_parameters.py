from fastapi import APIRouter
from src.schemas.message import MessageResponse
from src.services.parameters import load_config_from_firestore
router = APIRouter()

@router.get("/retrieve_params_firebase", response_model=MessageResponse)
async def retrieve_params_route():
    """Retrieve the model's parameters from Firebase.\n
    Returns a JSON containing the parameters or an error message.
    """
    params_message = load_config_from_firestore('parameters', 'model_parameters')
    return MessageResponse(message=params_message)
