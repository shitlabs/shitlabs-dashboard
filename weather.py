import requests
import time


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
    weather = get_weather()
    print(weather)
    time.sleep(60*60)


