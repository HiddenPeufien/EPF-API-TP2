from fastapi import APIRouter
from src.schemas.message import MessageResponse
from src.services.utils import divide_data
import json
router = APIRouter()

@router.get("/divide_dataset", response_model=MessageResponse)
async def divide_dataset_route() -> MessageResponse:
    """Divide the dataset into training and testing sets and return them in JSON format.\n
    Returns JSON containing the training and testing sets or an error message.
    """
    train_set, test_set = divide_data('src/data/Iris.csv')
    response_message = ""
    if test_set != "":
        dataset_parts = {
            'training_set': json.loads(train_set),
            'testing_set': json.loads(test_set)
        }
        response_message = json.dumps(dataset_parts)
    else:
        response_message = train_set 
    return MessageResponse(message=response_message)
