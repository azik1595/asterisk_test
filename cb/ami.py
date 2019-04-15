#!/usr/bin/python
# -*- codding: utf-8 -*-

import socket
from time import sleep

ami_cmd1 = '''Action: login
Events: off
Username: callbackuser
Secret: Passsssword\n\n'''

ami_cmd2 = '''Action: Originate
Channel: SIP/some_manager
Context: call_to_client
Exten: %s
Priority: 1
Callerid: 1112233
Timeout: 30000\n\n'''

def ConnectToAsterisk(number=None):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = '127.0.0.1'
    PORT = 5038

    s.connect((HOST, PORT))
    s.send(bytes(ami_cmd1, 'utf-8'))
    sleep(0.1)
    data = s.recv(1024)

    calldata = ami_cmd2 % number
    print(calldata)
    s.send(bytes(calldata, 'utf-8'))
    sleep(0.1)
    data = s.recv(1024)

    s.close()