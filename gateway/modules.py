#!/usr/bin/env python
import socket,sys,gateway_cfg,select
class webserver :
  def __init__(self,condition):
    #init
    self.con = condition
  def run(self):
    #run
    print("web server start!!")
class msgcenter :
  def __init__(self,condition):
    #init server setting
    self.con = condition
    try:
      print("start config")
      self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      self.server.setblocking(0)
      self.server.bind((gateway_cfg.address['host'],gateway_cfg.address['port']))
      self.server.listen(gateway_cfg.max_user)
    except socket.error as msg:
      print("[ERROR] %s\n" % msg)
      self.break_out = true
  def run(self):
    #start 
    while true:
      connection,address = self.server.accept()
      connection.close() 
