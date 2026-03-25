from fastapi import APIRouter
from src.core.use_cases.calculo_calorias import calculo_de_calorias
from pydantic import BaseModel

calculo_calorias_router = APIRouter()

class CuttingRequest(BaseModel):
    peso: float
    altura: float
    idade: int
    genero: str
    nivel_atividade: str
    deficit: float

@calculo_calorias_router.post("/cuttingcalories/")
def create_cutting_calories(request: CuttingRequest):
    result = calculo_de_calorias(
        request.peso,
        request.altura,
        request.idade,
        request.genero,
        request.nivel_atividade,
        request.deficit,
    )
    return {"calorias": result}