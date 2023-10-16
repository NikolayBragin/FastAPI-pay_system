from pydantic import BaseModel

# класс для валидации добавления карт
class CardAddModel(BaseModel):
    user_id: int
    card_number: int
    balance: float
    card_name: str
    exp_date: int
    cvv: int

# класс для валидации изменения дизайна карты
class EditCardModel(BaseModel):
    card_id: int
    design_path: str




