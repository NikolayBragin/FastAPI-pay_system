from fastapi import APIRouter

from datetime import datetime

from database.transferservice import create_transaction, cansel_transfer_db, get_card_transaction_db
from transfers import CanselTransactionModel, CreateTransactionModel

transaction_router = APIRouter(prefix='/transaction', tags=['Работа с платежами'])

# запрос на создание транзакции
@transaction_router.post('/create')
async def add_new_transaction(data: CreateTransactionModel):
    transaction_data = data.model_dump()
    result = create_transaction(**transaction_data)

    return {'status': 1, 'message': result}


# запрос на отмену транзакции
@transaction_router.post('/cansel')
async def cansel_transaction(data: CanselTransactionModel):
    cansel_data = data.model_dump()
    result = create_transaction(**cansel_data)

    return {'status': 1, 'message': result}

# запрос на получение всех транзакций определенной карты
@transaction_router.get('/monitoring')
async def grt_card_monitoring(card_id: int):
    result = get_card_transaction_db(card_from_id=card_id)

    return {'status': 1, 'message': result}
