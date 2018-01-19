import requests

url = "https://bvg-grabber-api.herokuapp.com/actual?station=Geygerstr"
response = requests.get(url)
response = response.json()

runter = False
hoch = False
for _ in response[0][1]:
    if "Sonnen" in _["end"] and not runter:
        print(_["remaining"])
        runter = True
    elif not hoch:
        print(_["remaining"])
        hoch = True

