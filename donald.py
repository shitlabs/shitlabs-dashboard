#!/usr/bin/env python3
import lxml.html
import requests
import client_example
import time

c = client_example.Communicator()

try:
    req = requests.get("https://twitter.com/realdonaldtrump")
    elements = lxml.html.document_fromstring(req.text)
    stream = elements.find_class("stream-items")[0]
    children = stream.getchildren()
    for child in children:
        if any(["pinned" in _ for _ in child.values()]):
            continue
        else:
            break

    elapsed = time.time() - int(child.find_class("_timestamp")[0].values()[1])
    elapsed /= 60
    print(elapsed)
    if (elapsed < 30):
        c.send_msg("6,FAST")
    elif (elapsed < 60):
        c.send_msg("6,SLOW")
    elif (elapsed < 120):
        c.send_msg("6,ON")
    else:
        c.send_msg("6,OFF")
except:
    c.send_msg("6,ERROR")

