import requests
import logging
from celery import shared_task
# from django.core.mail import send_mail

logger = logging.getLogger("api")


@shared_task  # В разработке
def get_exchange_rate():
    response = requests.get("https://api.nbrb.by/exrates/rates?periodicity=0")
    response = response.json()
    for res in response:
        print(res)
    return response


# В разработке
# send_mail("Subject here","Here is the message.","from@example.com",["to@example.com"], fail_silently=False,)
