#/usr/bin/env python
import sys,random
border=1000.0
tras_range=15.0
node_num=int(sys.argv[1])
bs_x=bs_y=border/2.0
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
def initial():
  global x,y,parent,connect,child,neighbor,dep_c,iso_c,dep
  for a in range(node_num):
    x[a]=random.random()*border
    y[a]=random.random()*border
    dep[a]=False
    
  print("Program Start")
  print("Let's find the neighbor!")
  neighbor=[]
  iso_c=0
  dep_c=0
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
  global c, child, parent, connect, rank, level
  for a in range(node_num):
    child[a]=0
    parent[a]=-1
    connect[a]=False
    rank[a]=0
    level[a]=0
  c=0
def print_result():
  print("Print result")
  temo=0
  max_l=0
  number=[0,0,0,0,0]
  for a in range(node_num):
    if(connect[a] and dep[a]):
      temo+=1
    if(level[a]>max_l):
      max_l=level[a]
    number[child[a]]+=1
  print("Connect Node:",c," Max Level:",max_l," Connected Dep node", temo)
  print("Childr numb 0: ",number[0], " 1: ",number[1]," 2: ",number[2]," 3: ",number[3]," 4: ",number[4])
  print("End!@@")
def con1():
  global c, child, parent, connect, limit, neighbor, level, rank, dep
  old_c=-1
  for a in range(node_num):
    if (dist(bs_x,x[a],bs_y,y[a])<=tras_range):
      connect[a]=True
      c+=1
      level[a]=1
  while old_c!=c:
    old_c=c
    for a in range(node_num):
      if(connect[a]==False and dep[a]==False):
        for b in neighbor[a]: 
          if(connect[b]==True and child[b]<limit and level[b]<255):
            connect[a]=True
            child[b]+=1
            level[a]=level[b]+1
            parent[a]=b
            c+=1
            break	
  for a in range(node_num):
    if(connect[a]==False and dep[a]==True):
      for b in neighbor[a]:
        if(connect[b]==True and child[b]<limit and level[b] <255):
          connect[a]=True
          child[b]+=1
          level[a]=level[b]+1
          parent[a]=b
          c+=1
          break
def con2():
  global c, child, parent, connect, limit, neighbor, level, rank, dep
  old_c=-1
  for a in range(node_num):
    if (dist(bs_x,x[a],bs_y,y[a])<=tras_range):
      connect[a]=True
      level[a]=1
      c+=1
      for b in neighbor[a]:
        if(dep[b]):
          connect[b]=True
          c+=1
          child[a]+=1
          level[b]=level[a]+1
          parent[b]=a
  while old_c!=c:
    old_c=c
    for a in range(node_num):
      if(connect[a]==False):
        for b in neighbor[a]: 
          if(connect[b]==True and child[b]<limit and level[b]<255):
            connect[a]=True
            level[a]=level[b]+1
            child[b]+=1
            parent[a]=b
            c+=1
            for d in neighbor[a]:
              if(dep[d]==True and connect[d]== False):
                connect[d]=True
                level[d]=level[a]+1
                c+=1
                child[a]+=1
                parent[d]=a
            break		
def con3():
  global c, child, parent, connect, limit, neighbor, level, rank, dep
  old_c=-1
  for a in range(node_num):
    if (dist(bs_x,x[a],bs_y,y[a])<=tras_range):
      connect[a]=True
      level[a]=1
      c+=1
      for b in neighbor[a]:
        if(dep[b]):
          connect[b]=True
          c+=1
          child[a]+=1
          rank[a]+=1
          level[b]=level[a]+1
          parent[b]=a
  for a in range(node_num):
    if(connect[a]==True):
      for b in neighbor[a]:
        if(connect[b]==False):
          rank[a]+=1
      if(rank[a]>limit):
        rank[a]=limit 
  while old_c!=c:
    old_c=c
    for a in range(node_num):
      if(connect[a]==False):
        temp_l=[]
        min_rank=5
        for b in neighbor[a]: 
          if(connect[b]==True and child[b]<limit and level[b]<255):
            temp_l.append(b)
            if(min_rank>rank[b]):
              min_rank=rank[b]
        if(len(temp_l)>0):
          min_level=255
          temp_k=[]
          for b in temp_l:
            if(rank[b]==min_rank):
              temp_k.append(b)
              if(min_level>level[b]):
                min_level=level[b]
          for b in temp_k:
            if(min_level==level[b]):
              connect[a]=True
              c+=1
              level[a]=level[b]+1
              child[b]+=1
              parent[a]=b
              break
          for d in neighbor[a]:
            if(dep[d]==True and connect[d]== False):
              connect[d]=True
              level[d]=level[a]+1
              rank[a]+=1
              c+=1
              child[a]+=1
              parent[d]=a
          for b in neighbor[a]:
            if(connect[b]==False):
              rank[a]+=1
          if(rank[a]>limit):
            rank[a]=limit
for k in range(30):
  initial()
  clear()
  con1()
  print_result()
  clear()
  con2()
  print_result()
  clear()
  con3()
  print_result()
