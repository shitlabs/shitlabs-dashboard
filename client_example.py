#!/usr/bin/env python3


import zmq




class Communicator:
    SERVER_ADDRESS = "tcp://127.0.0.1:12059"

    def __init__(self):
        context = zmq.Context()
        self.connection_set = False
        self.socket = context.socket(zmq.REQ)
        self.socket.connect(Communicator.SERVER_ADDRESS)
        self.connection_set = True



    def send_msg(self, command_string):
        """ Send Message to Server, returns true if message was accepted by server, hangs if no connection """
        if not self.connection_set:
            self.socket.connect(Communicator.SERVER_ADDRESS)
            
        #send message
        self.socket.send_string(command_string)
        #now wait for reply
        reply = self.socket.recv_string()
        return reply == "ack"


if __name__ == '__main__':

    c = Communicator()

    c.send_msg('FADE')
