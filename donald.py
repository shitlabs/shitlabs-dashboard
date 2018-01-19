# coding: utf-8
import lxml.html
import requests
import time

while True:
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
    print(elapsed / 60)
    time.sleep(60)
