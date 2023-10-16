from fastapi import APIRouter

from datetime import datetime

from card import CardAddModel, EditCardModel
from database.cardservice import get_exact_card_db, get_exact_user_cards_db, \
    add_card_db, delete_exact_card_db, \
    edit_card_design_db, check_card_info_db

card_router = APIRouter(prefix='/card', tags=['Работа с картами'])

# запрос на добавление карты
@card_router.post('/add')
async def add_new_card(data: CardAddModel):
    # Переводим пайдентик на обычный ловарь
    card_data = data.model_dump()

    # проверка карты на наличие в базе
    checker = check_card_info_db(data.card_number)

    # Если есть карта в базе, то не регестрируем
    if checker:
        return {'status': 1, 'message': "Карта с таким номером есть в базе "}

    else:
        result = add_card_db(**card_data)

        return {'status': 1, 'message': result}


# запрос на получение информации о карте
@card_router.get('/exact-card-info')
async def get_card_info(card_id: int, user_id: int):
    result = get_exact_card_db(card_id=card_id, user_id=user_id)

    if result:
        return {'status': 1, 'message': result}

    return {'status': 0, 'message': "Карта не найдена"}

# запрос на получение всех карт пользователя
@card_router.get('/get-info')
async def get_all_user_cards(user_id: int):
    result = get_exact_user_cards_db(user_id=user_id)

    return {'status': 1, 'message': result}


# запрос на удаление карты
@card_router.delete('/delete-card')
async def delete_exact_card(card_id: int):
    result = delete_exact_card_db(card_id=card_id)

    return {'status': 1, 'message': result}

# запрос на изменение дизайна карт
@card_router.put('/edit-card-design')
async def edit_card_design(data: EditCardModel):
    # Переводим пайдентик на обычный ловарь
    design_data = data.model_dump()

    result = edit_card_design_db(**design_data)

    return {'status': 1, 'message': result}
