import zmq
import logging
import threading
from time import sleep, time

def zero():
    while True:
        yield (0,0,0)

def white():
    while True:
        yield (255,255,255)

leds = [zero()]*8


def run_server():
    global leds
    logger = logging.getLogger()
    context = zmq.Context()

    update_needed = False

    socket_rep = context.socket(zmq.REP)

    socket_rep.bind("tcp://127.0.0.1:12059")

    logger.debug("Bound REP socket to localhost port 12059")


    while True:
        msg = socket_rep.recv_string()
        logger.debug("Received Message: %s" % msg)
        if "," in msg:
            command = [x.strip() for x in msg.split(',')]
            logger.debug("Interpreted command: %s" % command[0])
            # now dispatch messages...
            if command[0] == "WHITE":
                logger.debug("Setting LED %d to white" % int(command[1]))
                leds[int(command[1])] = white()
            if command[0] == "BLACK":
                leds[int(command[1])] = zero()

            socket_rep.send_string("ack")

        else:
            logger.debug("Obviously not a command...")
            # send beg an error
            socket_rep.send_string("err")

def simulator():
    global leds
    fps = 1
    while True:
        tic = time()
        rgbs = [next(x) for x in leds]
        [print("#%02X%02X%02X" %rgb,end="\t") for rgb in rgbs]
        print("", flush=True)
        left = 1/fps - (time()-tic)
        if left>0:
            sleep(left)




def prepare():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    hw = threading.Thread(target=simulator)
    api = threading.Thread(target=run_server)
    hw.start()
    api.start()
    hw.join()
    api.join()






        

if __name__ == "__main__":
    prepare()
