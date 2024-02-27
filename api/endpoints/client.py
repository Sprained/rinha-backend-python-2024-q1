from fastapi import APIRouter, Body, Depends, Query
from sqlalchemy.orm import Session

from interfaces.transaction import CreateTransactionDto
from interfaces.responses import ErrorResponseDto
from db.database import DatabaseUtils

router = APIRouter(prefix="/clientes")

@router.post(
    "/{client_id}/transacoes",
    summary="Create a new transaction",
    status_code=200,
    response_description="Successfully create a new transaction",
    responses={400: {"model": ErrorResponseDto}},
)
def transaction(
    client_id: int, data: CreateTransactionDto, db: Session = Depends(DatabaseUtils.get_db)
):
    print("teste")
    return