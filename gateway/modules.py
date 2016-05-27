#!/usr/bin/env python
import socket,sys,gateway_cfg,queue,select
active_module=[]
class webserver :
  def __init__():
    
class msgcenter :
  def __init__():
  def

if __name__ == '__main__'
  try:
    print("Hello World!!")
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.setblocking(0)
    server.bind((gateway_cfg.address['host'],gateway_cfg.address['port']))
    print("Port",gateway_cfg.address['port'])
    server.listen(gateway_cfg.max_user)
    while true:
      connection,address = sock.accept()
      connection.close()
  except socket.error as msg:
    sys.stderr.write("[ERROR] %s\n" % msg)
    sys.exit(1)
  except KeyboardInterrupt:
    server.close()
    exit(0)
  except:
    exit(0)
