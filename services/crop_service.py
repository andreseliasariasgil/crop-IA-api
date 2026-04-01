import joblib
import numpy as np
import os

# Ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

rf_path = os.path.join(BASE_DIR, "RFCosecha.pkl")
svm_path = os.path.join(BASE_DIR, "SVMCosecha.pkl")

# Cargar modelos correctamente (IMPORTANTE: usar joblib)
rf_model = joblib.load(rf_path)
svm_model = joblib.load(svm_path)

# Predicción RandomForest
def predict_rf(data):
    xin = np.array([[ 
        data.N,
        data.P,
        data.K,
        data.temperature,
        data.humidity,
        data.ph,
        data.rainfall
    ]])
    
    prediction = rf_model.predict(xin)
    return prediction[0]

# Predicción SVM
def predict_svm(data):
    xin = np.array([[ 
        data.N,
        data.P,
        data.K,
        data.temperature,
        data.humidity,
        data.ph,
        data.rainfall
    ]])
    
    prediction = svm_model.predict(xin)
    return prediction[0]