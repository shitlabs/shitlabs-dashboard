import zmq

class Communicator:
    SERVER_ADDRESS = "tcp://127.0.0.1:12059"

    def __init__(self):
        context = zmq.Context()
        self.connection_set = False
        self.socket = context.socket(zmq.REQ)
        self.socket.connect(SERVER_ADDRESS)
        self.connection_set = True



    def send_msg(self, command_string):
        if not self.connection_set:
            self.socket.connect(SERVER_ADDRESS)
            
        #send message
        self.socket.send_string(command_string)
        #now wait for reply
        reply = self.socket.recv_string()
        return reply == "ack"

