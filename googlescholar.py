import lxml.html
import requests
import time

def get_citation_count():
    req = requests.get("https://scholar.google.de/citations?user=3SsX1ecAAAAJ")
    elements = lxml.html.document_fromstring(req.text)
    stream = elements.get_element_by_id("gsc_rsb_st")
    value = int(stream.find_class("gsc_rsb_std")[0].text)
    return value

current_count = get_citation_count()

while True:
    next_count = get_citation_count()
    if next_count != current_count:
        print(next_count)
        current_count = next_count
    else:
        print("no change")
    time.sleep(60*60)
