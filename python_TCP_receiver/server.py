#
#   Hello World server in Python
#   Binds REP socket to tcp://192.168.195.3:5555
#   Expects b"Hello" from client, replies with b"World"
#
 
import time
import zmq
import pickle
import numpy as np
import datetime
 
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
#socket.bind("tcp://192.168.132.113:5555")
now = datetime.datetime.now()
filename = 'unlabeled/log_' + now.strftime('%Y%m%d_%H%M%S') + '.txt'

file = open(filename, "wb")
 
while True:
    #  Wait for next request from client
    message = socket.recv()
    #print(message)
    d = pickle.loads(message)
    #  Do some 'work'
    #time.sleep(1)
    np.savetxt(file, d, delimiter=",", fmt='%.3f', newline='\n')
    #  Send reply back to client
    socket.send(b"World")