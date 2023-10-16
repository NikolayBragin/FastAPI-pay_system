from fastapi import APIRouter, Depends
import requests

from reddis_service import redis_db

currency_router = APIRouter(prefix='/currency', tags=['Курсы валют'])

# проверка редис есть ли там информация про курс валют
def _check_currency_rates_redis():
    usd = redis_db.get("USD")
    rub = redis_db.get("RUB")
    eur = redis_db.get("EUR")
    jpy = redis_db.get("JPY")

    if usd and rub and eur and jpy:
        return {'USD': usd.decode(), 'RUB': rub.decode(), 'JPY': jpy.decode(), 'EUR': eur.decode()}

    return False

# запрос на получение всех курсов валют
@currency_router.post(('/get-rates'))
async def get_currency_rates(redis_checker=Depends(_check_currency_rates_redis)):
    # если в редисе есть данныеб то показываем оттуда
    if redis_checker:
        return {'status': 1, 'rates': redis_checker}
    # а если в релисе ничего нет, переходим по ссылке и записываем
    cb_url = 'https://cbu.uz/ru/arkhiv-kursov-valyut/json/'
    response = requests.get(cb_url).json()

    # созраняем только те валюты которые нам нужны
    usd_eur_rub_jpy = [i for i in response if i['Ccy'] in ['EUR', 'RUB', 'USD', 'JPY']]
    # сохраним в редис базу
    redis_db.set("USD", usd_eur_rub_jpy[0]["Rate"], 5)
    redis_db.set("EUR", usd_eur_rub_jpy[1]["Rate"], 5)
    redis_db.set("RUB", usd_eur_rub_jpy[2]["Rate"], 5)
    redis_db.set("JPY", usd_eur_rub_jpy[3]["Rate"], 5)

    return {'status': 1, 'rates': usd_eur_rub_jpy}



# запрос на получение определенного курса
