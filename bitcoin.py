import requests
import time
import client_example


def get_yesterdays_closing():
    url = "https://api.coindesk.com/v1/bpi/historical/close.json?for=yesterday"
    response = requests.get(url)
    return list(response.json()["bpi"].values())[0]


def get_current_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    return response.json()["bpi"]["USD"]["rate_float"]

c = client_example.Communicator()

while True:
    reference = get_yesterdays_closing()
    current = get_current_price()
    if (current / reference - 1)  > 0:
        c.send_msg("COLOR,0,00cc00")
    else:
        c.send_msg("COLOR,0,cc0000")
    time.sleep(60)
