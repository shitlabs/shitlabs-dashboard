import lxml.html
import requests
import time
import client_example

def get_citation_count():
    req = requests.get("https://scholar.google.de/citations?user=3SsX1ecAAAAJ")
    elements = lxml.html.document_fromstring(req.text)
    stream = elements.get_element_by_id("gsc_rsb_st")
    value = int(stream.find_class("gsc_rsb_std")[0].text)
    return value


c = client_example.Communicator()

while True:
    try:
        try:
            with open("michis_score.txt", "r") as f:
                current_score,last_status,days_on= f.read().split(",")
                current_score = int(current_score)
                days_on = int(days_on)
        except:
            current_score = get_citation_count()
            last_status = "OFF" 
            days_on = 0

        next_score = get_citation_count()
        print(current_score, last_status, days_on)
        if next_score != current_score:
            c.send_msg("7,FAST")
            current_score = next_score
            last_status = "FAST"
            days_on = 0
        elif last_status == "FAST":
            c.send_msg("7,SLOW")
            last_status = "SLOW"
            days_on = 0
        elif last_status == "SLOW":
            last_status = "ON"
            c.send_msg("7,ON")
            days_on += 1
        elif last_status == "ON" and days_on < 5:
            c.send_msg("7,ON")
            days_on += 1
        else:
            c.send_msg("7,OFF")
            last_status = "OFF"
            days_on = 0

        with open("michis_score.txt", "w") as f:
            outstring = "{0},{1},{2}".format(current_score,last_status,days_on)
            f.write(outstring)
    except:
        c.send_msg("7,ERROR")
    time.sleep(60*60*24)
