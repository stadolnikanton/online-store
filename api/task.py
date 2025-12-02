import requests
import logging
from celery import shared_task
from django.core.cache import cache


logger = logging.getLogger("api")


@shared_task
def get_exchange_rate():
    cache_key = "exchange_rates_data"
    cached_data = cache.get(cache_key)

    if cached_data:
        return cached_data
    try:
        response = requests.get(
            "https://api.nbrb.by/exrates/rates?periodicity=0", timeout=10
        )
        response.raise_for_status()

        data = response.json()

        cache.set(cache_key, data, 60 * 15)

        for res in data:
            print(f"{res.get('Cur_Name')}: {res.get('Cur_OfficialRate')}")
        return data

    except requests.exceptions.RequestException:
        return None
