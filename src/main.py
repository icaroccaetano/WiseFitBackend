from fastapi import FastAPI
from src.presentation.api.v1.calculo_calorias import calculo_calorias_router
from fastapi.middleware.cors import CORSMiddleware
from src.presentation.api.v1.calculo_macros import calculo_macros_router

app = FastAPI(title="Cutting API")

origins = [
    "http://localhost:3000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de Cutting"}

app.include_router(calculo_calorias_router)
app.include_router(calculo_macros_router)
