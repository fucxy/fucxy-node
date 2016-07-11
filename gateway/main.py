#!/usr/bin/env python
import sys,gateway_cfg,os,modules
from threading import *
try:
  if __name__ == "__main__":
    cond = Condition()
    for s in gateway_cfg.script_aquire:
      s(cond).start()
    while True:
      pass
except KeyboardInterrupt:
  print("Keyboard stop!!")
  exit(0)
except:
  exit(0)
