import requests
import time
import client_example 

c = client_example.Communicator()

def get_weather():
    url ="https://query.yahooapis.com/v1/public/yql?q=select%20item."\
          "condition%20from%20weather.forecast%20where%20woeid%20%3D%"\
          "20638242&format=json&env=store%3A%2F%2Fdatatables.org%2Fall"\
          "tableswithkeys"
    response = requests.get(url).json()
    temp = response["query"]["results"]["channel"]["item"]["condition"]["temp"]
    temp = (float(temp) - 32) / 1.8
    return temp

while True:
    try:
        weather = get_weather()
        if weather <= 0:
            c.send_msg("2,FAST")
            c.send_msg("5,OFF")
        elif weather < 5:
            c.send_msg("2,SLOW")
            c.send_msg("5,OFF")
        elif weather < 10:
            c.send_msg("2,ON")
            c.send_msg("5,OFF")
        elif weather < 15:
            c.send_msg("2,ON")
            c.send_msg("5,ON")
        elif weather < 20:
            c.send_msg("2,OFF")
            c.send_msg("5,ON")
        elif weather < 25:
            c.send_msg("2,OFF")
            c.send_msg("5,SLOW")
        else:
            c.send_msg("2,OFF")
            c.send_msg("5,FAST")
    except:
        c.send_msg("2,ERROR")
        c.send_msg("5,ERROR")

    time.sleep(60*60)
