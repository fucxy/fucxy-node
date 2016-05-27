#!/usr/bin/env python
import sys,gateway_cfg,os
from threading import *

class Threadbase(Thread):
  def __init__(self,string,condition):
    Thread.__init__(self)
    self.con = condition
    self.path = string
  def run(self):
    #run something
    print("",self.path)

try:
  if __name__ == "__main__":
    cond = Condition()
    for s in gateway_cfg.script_aquire:
      Threadbase(s,cond ).start()

    while True:
      pass
except KeyboardInterrupt:
  print("Keyboard stop!!")
  exit(0)
except:
  exit(0)
