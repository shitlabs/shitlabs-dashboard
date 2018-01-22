#!/usr/bin/env python3
import requests
import client_example


def get_pattern(remaining):
    if remaining <= 1:
        return "FAST"
    elif remaining <= 4:
        return "SLOW"
    elif remaining <= 10:
        return "ON"
    else:
        return "OFF"


c = client_example.Communicator()


try:
    url = "https://bvg-grabber-api.herokuapp.com/actual?station=Geygerstr"
    response = requests.get(url)
    response = response.json()
    
    runter = False
    hoch = False
    for _ in response[0][1]:
        remaining = _["remaining"] / 60
        pattern = get_pattern(remaining)
        if "Sonnen" in _["end"] and not runter:
            c.send_msg("4,"+pattern)
            runter = True
            print("Runter: ", remaining)
        elif not hoch:
            c.send_msg("1,"+pattern)
            hoch = True
            print("Hoch: ", remaining)
except:
    c.send_msg("4,ERROR")
    c.send_msg("1,ERROR")

