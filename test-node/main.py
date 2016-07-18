#!/usr/bin/env python
import socket,sys
UDP_IP = "127.0.0.1"
UDP_PORT = 8888
try:
  sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  sock.bind((UDP_IP,UDP_PORT))
  while True:
    data.addr = sock.recvfrom(1024)
    print ("Recv:",data)
except KeyboardInterrupt:
  print("Keyboard stop!")
  exit(0)
#except:
#  exit(0)
