#!/usr/bin/env python
import socket,sys,gateway_cfg,select,socketserver,http.server,urllib
from threading import *
class WebHandler(http.server.BaseHTTPRequestHandler):
  def do_GET(self):
    parseParams = urllib.parse.urlparse(self.path) 
    if parseParams.path=="/t" :
      self.send_error(404,"You can't pass!!")
    else:
      self.send_response(200)
      self.send_header('Content-Type', 'application/html')
      self.end_headers()
      self.wfile.write("Hello World!!")
      self.wfile.close()
class webserver (Thread):
  def __init__(self,condition):
    #init
    Thread.__init__(self)
    self.con = condition
  def run(self):
    #run
    print("web server start!!")
    Handler = WebHandler
    httpd = http.server.HTTPServer(("", 8080), Handler)
    httpd.serve_forever()
class msgcenter (Thread):
  def __init__(self,condition):
    #init server setting
    Thread.__init__(self)
    self.con = condition
    try:
      print("start config")
      self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      self.server.bind((gateway_cfg.address['host'],gateway_cfg.address['port']))
      self.server.listen(gateway_cfg.max_user)
      self.break_out = False
    except socket.error as msg:
      print("[ERROR] %s\n" % msg)
      self.break_out = True
  def run(self):
    #start 
    if self.break_out == False:
      print("msgcenter start!!")
      while True:
        try:
          connection,address = self.server.accept()
          connection.setblocking(0)
          connection.close()
        except IOError as e:
          if e.errno == 11:
            raise
          else:
            print("socket error")
            exit(-1)
