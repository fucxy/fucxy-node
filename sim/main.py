#/usr/bin/env python
import sys,random
border=500.0
tras_range=15.0
node_num=10000
bs_x=bs_y=border/2
x=[random.random()*border for a in range(node_num)]
y=[random.random()*border for a in range(node_num)]
parent=[-1 for a in range(node_num)]
connect=[False for a in range(node_num)]
child=[0 for a in range(node_num)]
limit=4
c=0
def dist(x1,x2,y1,y2,):
  return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
#base station
print("Program Start")
for a in range(node_num):
  if (dist(bs_x,x[a],bs_y,y[a])<=tras_range):
    connect[a]=True
    c+=1
print("1st connected node:",c)
def con():
  global c
  global child
  global parent
  global connect
  global limit
  
  for a in range(node_num):
    if(connect[a]==False):
      for b in range(node_num): 
        if(a!=b and connect[b]==True and child[b]<=limit and dist(x[a],x[b],y[a],y[b])<=tras_range):
          connect[a]=True
          child[b]+=1
          parent[a]=b
          c+=1
          break
  print("connected node:",c)
con()
con()
  
