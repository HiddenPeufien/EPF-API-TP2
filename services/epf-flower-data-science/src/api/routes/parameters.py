from fastapi import APIRouter
from src.schemas.message import MessageResponse
from src.services.parameters import load_configurations

router = APIRouter()

@router.get("/fetch_model_params", response_model=MessageResponse)
async def model_parameters_route():
    """Retrieve the configuration parameters for the model.\n
    Returns a JSON containing the parameters or an error message.
    """
    model_params = load_configurations('src/config/model_config.json')
    return MessageResponse(message=model_params)
