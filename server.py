#!/usr/bin/env python3
import zmq
import logging
import threading
import time
#import shitlight_simulator as shitlight
import shitlight
import random

from fade_pattern import FadePattern

leds = [0] * 9

led_colors = [(0, 255, 0),
              (0, 0, 255),
              (0, 0, 255),
              (255, 0, 0),
              (0, 0, 255),
              (255, 0, 0),
              (255, 0, 0),
              (0, 255, 0),
              (0, 255, 0)
             ]


def run_server():
    global leds
    logger = logging.getLogger()
    context = zmq.Context()

    update_needed = False

    socket_rep = context.socket(zmq.REP)

    socket_rep.bind("tcp://127.0.0.1:12059")

    #logger.debug("Bound REP socket to localhost port 12059")
    while True:
        msg = socket_rep.recv_string()
        #logger.debug("Received Message: %s" % msg)
        if "," in msg:
            try:
                command = [x.strip() for x in msg.split(',')]
                # logger.debug("Interpreted command: %s" % command[0])
                # now dispatch messages...
                if command[1] == "ON":
                    leds[int(command[0])] = 1

                elif command[1] == "OFF":
                    leds[int(command[0])] = 0

                elif command[1] == "SLOW":
                    leds[int(command[0])] = 2

                elif command[1] == "FAST":
                    leds[int(command[0])] = 3

                elif command[1] == "ERROR":
                    leds[int(command[0])] = 4
    
            except:
                socket_rep.send_string("err")
                raise
            else:
                socket_rep.send_string("ack")

        else:
            # logger.debug("Obviously not a command...")
            # send beg an error
            socket_rep.send_string("err")

def simulator():
    global leds
    fps = 8

    dashboard = shitlight.Dashboard()

    while True:
        tic = time.time()

        for frame in range(fps):
            rgbs = []
            for _, status in enumerate(leds):
                r, g, b = led_colors[_]
                ran = random.random()
                if status < 2:
                    rgbs.append((r * status, g * status, b * status))
                if status == 2 and frame < 0.5 * fps:
                    rgbs.append((r,g,b))
                if status == 2 and frame >= 0.5 * fps:
                    rgbs.append((0,0,0))
                if status == 3 and (frame < 0.25 * fps):
                    rgbs.append((r,g,b))
                if status == 3 and (frame >= 0.5 * fps) and (frame < 0.75 * fps):
                    rgbs.append((r,g,b))
                if status == 3 and (frame >= 0.25 * fps) and (frame < 0.5 * fps):
                    rgbs.append((0,0,0))
                if status == 3 and (frame >= 0.75 * fps):
                    rgbs.append((0,0,0))
                if status == 4 and ran < 0.5:
                    rgbs.append((r,g,b))
                if status == 4 and ran >= 0.5:
                    rgbs.append((0,0,0))

            dashboard.set_color(rgbs)
            time.sleep(1/fps)

#        left = 1/fps - (time()-tic)
#        if left>0:
#            sleep(left)


def prepare():
    #logger = logging.getLogger()
    #logger.setLevel(logging.DEBUG)
    hw = threading.Thread(target=simulator)
    api = threading.Thread(target=run_server)
    hw.start()
    api.start()
    hw.join()
    api.join()


if __name__ == "__main__":
    prepare()
