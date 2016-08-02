#/usr/bin/env python
import sys,random
border=1000.0
tras_range=15.0
node_num=10000
bs_x=bs_y=border/2
x=[random.random()*border for a in range(node_num)]
y=[random.random()*border for a in range(node_num)]
parent=[-1 for a in range(node_num)]
neighbor=[]
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
print("base station connected node:",c)
print("Let's find the neighbor!")
for a in range(node_num):
  temp_l=[]
  for b in range(node_num):
    if(a!=b and dist(x[a],x[b],y[a],y[b])<=tras_range):
      temp_l.append(b) 
  neighbor.append(temp_l)
print("the neighbor find end!!")
def con():
  global c
  global child
  global parent
  global connect
  global limit
  global neighbor
  for a in range(node_num):
    if(connect[a]==False):
      for b in neighbor[a]: 
        if(connect[b]==True and child[b]<=limit and dist(x[a],x[b],y[a],y[b])<=tras_range):
          connect[a]=True
          child[b]+=1
          parent[a]=b
          c+=1
          break
  print("connected node:",c)
con()
con()
con()
con()
  
