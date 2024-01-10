"""API Router for Fast API."""
from fastapi import APIRouter

from src.api.routes import hello, data, load, processing, split, train, predict, parameters, firebase_parameters

router = APIRouter()

router.include_router(hello.router, tags=["Hello"])
router.include_router(data.router, tags=["Download Data"])
router.include_router(load.router, tags=["Load Dataset"])
router.include_router(processing.router, tags=["Processed Dataset"])
router.include_router(split.router, tags=["Split Dataset"])
router.include_router(parameters.router, tags=["Get Parameters"])
router.include_router(firebase_parameters.router, tags=["Firebase, not working because i didn't want my ID to be on the git"])
router.include_router(train.router, tags=["Train"])
router.include_router(predict.router, tags=["Predict"])

