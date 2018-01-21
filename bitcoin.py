#!/usr/bin/env python3
import requests
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


try:
    reference = get_yesterdays_closing()
    current = get_current_price()
    change = (current / reference - 1) 
    print(change)
    if change > 0.1:
        c.send_msg("0,FAST")
        c.send_msg("3,OFF")
    if (change <= 0.1) and (change > 0.05):
        c.send_msg("0,SLOW")
        c.send_msg("3,OFF")
    if (change > 0.005) and (change <= 0.05):
        c.send_msg("0,ON")
        c.send_msg("3,OFF")
    if (change <= 0.005) and (change >= -0.005):
        c.send_msg("0,OFF")
        c.send_msg("3,OFF")
    if (change < -0.005) and (change >= -0.05):
        c.send_msg("0,OFF")
        c.send_msg("3,ON")
    if (change < -0.05) and (change >= -0.5):
        c.send_msg("0,OFF")
        c.send_msg("3,SLOW")
    if (change < -0.1):
        c.send_msg("0,OFF")
        c.send_msg("3,FAST")
except:
    c.send_msg("0,ERROR")
    c.send_msg("3,ERROR")

