from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.crop_router import router

# Crear app
app = FastAPI(
    title="IA Recomendación de Cultivos",
    description="API para predicción usando RandomForest y SVM",
    version="1.0"
)

# 🔥 CONFIGURACIÓN CORS (MUY IMPORTANTE)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # permite frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rutas
app.include_router(router)

# Ruta de prueba
@app.get("/")
def home():
    return {"message": "API de cultivos funcionando 🚀"}