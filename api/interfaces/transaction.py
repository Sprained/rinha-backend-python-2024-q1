from pydantic import BaseModel, Field
from typing_extensions import Literal

class CreateTransactionDto(BaseModel):
    valor: int = Field(...)
    tipo: Literal["c", "d"] = Field(...)
    descricao: str = Field(..., max_length=10)