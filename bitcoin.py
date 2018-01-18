import requests
import time


def get_yesterdays_closing():
    url = "https://api.coindesk.com/v1/bpi/historical/close.json?for=yesterday"
    response = requests.get(url)
    return list(response.json()["bpi"].values())[0]

def get_current_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    return response.json()["bpi"]["USD"]["rate_float"]

while True:
    reference = get_yesterdays_closing()
    current = get_current_price()
    print(current / reference - 1)
    time.sleep(60)


