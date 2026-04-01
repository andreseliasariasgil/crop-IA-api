from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.crop_router import router

# Crear aplicación FastAPI
app = FastAPI(
    title="IA Recomendación de Cultivos",
    description="API para predicción usando RandomForest y SVM",
    version="1.0",
    docs_url="/docs",          # Swagger
    redoc_url="/redoc",        # Documentación alternativa
    openapi_url="/openapi.json"  # 🔥 importante para Render
)

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Permitir frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rutas
app.include_router(router)

# Ruta principal
@app.get("/")
def home():
    return {
        "message": "API de cultivos funcionando 🚀",
        "docs": "/docs",
        "endpoints": [
            "/predict/rf",
            "/predict/svm"
        ]
    }