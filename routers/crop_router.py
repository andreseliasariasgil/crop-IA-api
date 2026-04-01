from fastapi import APIRouter
from schemas.crop_schema import CropData
from services.crop_service import predict_rf, predict_svm

router = APIRouter()

@router.post("/predict/rf")
async def predict_random_forest(data: CropData):
    result = predict_rf(data)
    return {
        "model": "RandomForest",
        "prediction": result
    }

@router.post("/predict/svm")
async def predict_svm_model(data: CropData):
    result = predict_svm(data)
    return {
        "model": "SVM",
        "prediction": result
    }