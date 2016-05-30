#!/usr/bin/env python
import sys,gateway_cfg,os,modules
from threading import *

class Threadbase(Thread):
  def __init__(self,instant,condition):
    Thread.__init__(self)
    self.con = condition
    self.path = instant
    print(instant)
    self.ob = instant(condition)
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
