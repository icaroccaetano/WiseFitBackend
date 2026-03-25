from fastapi import APIRouter
from src.core.use_cases.calculo_macros import calculo_de_macros
from pydantic import BaseModel

calculo_macros_router = APIRouter()

class CuttingMacrosRequest(BaseModel):
    peso: float
    calorias: float

@calculo_macros_router.post("/cuttingmacros/")
def create_cutting_macros(request: CuttingMacrosRequest):
    result = calculo_de_macros(
        request.calorias,
        request.peso,
    )
    return result