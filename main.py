from fastapi import FastAPI

# Если хотим выводить html странички
from starlette.templating import Jinja2Templates


from user.user_api import user_router
from card.card_api import card_router
from transfers.transfers_api import transaction_router
from currency.currency_api import currency_router

# Создать базу данных
from database import Base, engine
Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')

## Если хотим выводить html странички
template = Jinja2Templates(directory='templates')
from html_example.html_show import html_router
app.include_router(html_router)
## Если хотим выводить html странички

# Регистрация компонента
app.include_router(user_router)
app.include_router(card_router)
app.include_router(transaction_router)
app.include_router(currency_router)


