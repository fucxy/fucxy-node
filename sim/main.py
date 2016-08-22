#/usr/bin/env python
import sys,random
border=1000.0
tras_range=15.0
node_num=10000
bs_x=bs_y=0.0
x=[random.random()*border for a in range(node_num)]
y=[random.random()*border for a in range(node_num)]
parent=[-1 for a in range(node_num)]
neighbor=[]
connect=[False for a in range(node_num)]
child=[0 for a in range(node_num)]
limit=4
rank=[0 for a in range(node_num)]
level=[0 for a in range(node_num)]
c=0
iso_c=0
dep_c=0
dep=[False for a in range(node_num)]
def dist(x1,x2,y1,y2):
  return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
#base station
print("Program Start")
print("Let's find the neighbor!")
for a in range(node_num):
  temp_l=[]
  for b in range(node_num):
    if(a!=b and dist(x[a],x[b],y[a],y[b])<=tras_range):
      temp_l.append(b) 
  neighbor.append(temp_l)
  if(len(temp_l)==0):
    iso_c+=1
  if(len(temp_l)==1):
    dep[a]=True
    dep_c+=1
print("Total nodes:",node_num," isolated node:",iso_c," depended node:",dep_c)
print("the neighbor find end!!")
def clear():
  global c
  global child
  global parent
  global connect
  for a in range(node_num):
    child[a]=0
    parent[a]=-1
    connect[a]=False
    rank[a]=0
    level[a]=0
  c=0
def print_result():
  print("Print result")
def con1():
  global c
  global child
  global parent
  global connect
  global limit
  global neighbor
  old_c=-1
  for a in range(node_num):
    if (dist(bs_x,x[a],bs_y,y[a])<=tras_range):
      connect[a]=True
      c+=1
  while old_c!=c:
    old_c=c
    for a in range(node_num):
      if(connect[a]==False and len(neighbor[a])!=1):
        for b in neighbor[a]: 
          if(connect[b]==True and child[b]<limit and dist(x[a],x[b],y[a],y[b])<=tras_range):
            connect[a]=True
            child[b]+=1
            parent[a]=b
            c+=1
            break	
  temo=0
  for a in range(node_num):
    if(connect[a]==True and dep[a]==True):
      temo+=1
  
  print("connected node:",c," isolated node:",iso_c," depended node:",temo)
def con2():
  global c
  global child
  global parent
  global connect
  global limit
  global neighbor
  old_c=-1
  for a in range(node_num):
    if (dist(bs_x,x[a],bs_y,y[a])<=tras_range):
      connect[a]=True
      c+=1
      for b in neighbor[a]:
        if(dep[b]):
          connect[b]=True
          c+=1
          child[a]+=1
          parent[b]=a
  while old_c!=c:
    old_c=c
    for a in range(node_num):
      if(connect[a]==False):
        for b in neighbor[a]: 
          if(connect[b]==True and child[b]<limit and dist(x[a],x[b],y[a],y[b])<=tras_range):
            connect[a]=True
            child[b]+=1
            parent[a]=b
            c+=1
            for d in neighbor[b]:
              if(dep[d] and connect[d]== False):
                connect[d]=True
                c+=1
                child[b]+=1
                parent[d]=b
            break		
  temo=0
  for a in range(node_num):
    if(connect[a]==True and dep[a]==True):
      temo+=1
  print("connected node:",c," isolated node:",iso_c," depended node:",temo)
def con3():
  global c
  global child
  global parent
  global connect
  global limit
  global neighbor
  old_c=-1
  for a in range(node_num):
    if (dist(bs_x,x[a],bs_y,y[a])<=tras_range):
      connect[a]=True
      level[a]=1
      c+=1
      for b in neighbor[a]:
        if(dep[b]):
          connect[b]=True
          level[b]=2
          c+=1
          child[a]+=1
          parent[b]=a
  while old_c!=c:
    old_c=c
    for a in range(node_num):
      if(connect[a]==False):
        for b in neighbor[a]: 
          if(connect[b]==True and child[b]<limit and dist(x[a],x[b],y[a],y[b])<=tras_range):
            connect[a]=True
            child[b]+=1
            parent[a]=b
            c+=1
            for d in neighbor[b]:
              if(dep[d] and connect[d]== False):
                connect[d]=True
                c+=1
                child[b]+=1
                parent[d]=b
            break		
  print("connected node:",c," isolated node:",iso_c," depended node:",dep_c)
con1()
clear()
con2()
clear()
con3()

