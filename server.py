import zmq
import logging
from time import sleep

def run_server():
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
            socket_rep.send_string("ack")

        else:
            logger.debug("Obviously not a command...")
            # send beg an error
            socket_rep.send_string("err")


        

if __name__ == "__main__":
    run_server()
