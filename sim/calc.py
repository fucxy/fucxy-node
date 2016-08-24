#/usr/bin/env python
import sys,random
f=open(sys.argv[1],'r')
iso_num=0
dep_num=0
con_num=[0,0,0]
max_level=[0,0,0]
con_dep=[0,0,0]
chi_0=[0,0,0]
chi_1=[0,0,0]
chi_2=[0,0,0]
chi_3=[0,0,0]
chi_4=[0,0,0]
for a in range(30):
  line=f.readline()
  line=f.readline()
  line=str(f.readline())
  for c in range(6):
    line=line[line.index(" ")+1:] 
  iso_num+=int(line[:line.index(" ")])
  for c in range(4):
    line=line[line.index(" ")+1:] 
  dep_num+=int(line)
  line=f.readline()
  for b in range(3):
    line=f.readline()
    line=str(f.readline())
    for c in range(2):
      line=line[line.index(" ")+1:] 
    con_num[b]+=int(line[:line.index(" ")])
    for c in range(4):
      line=line[line.index(" ")+1:] 
    max_level[b]+=int(line[:line.index(" ")])
    for c in range(5):
      line=line[line.index(" ")+1:]
    con_dep[b]+=int(line)
    line=str(f.readline())
    for c in range(4):
      line=line[line.index(" ")+1:]
    chi_0[b]+=int(line[:line.index(" ")])
    for c in range(4):
      line=line[line.index(" ")+1:]
    chi_1[b]+=int(line[:line.index(" ")])
    for c in range(4):
      line=line[line.index(" ")+1:]
    chi_2[b]+=int(line[:line.index(" ")])
    for c in range(4):
      line=line[line.index(" ")+1:]
    chi_3[b]+=int(line[:line.index(" ")])
    for c in range(4):
      line=line[line.index(" ")+1:]
    chi_4[b]+=int(line)
    line=f.readline()
f.close()
print("isolated node:",iso_num/30)
print("dep node:",dep_num/30)
print("Connect num: ",con_num[0]/30," ",con_num[1]/30," ",con_num[2]/30)
print("max_level: ",max_level[0]/30," ",max_level[1]/30," ",max_level[2]/30)
print("Con Dep: ",con_dep[0]/30," ",con_dep[1]/30," ",con_dep[2]/30)
print("max_level: ",max_level[0]/30," ",max_level[1]/30," ",max_level[2]/30)
print("child num0: ",chi_0[0]/30," ",chi_0[1]/30," ",chi_0[2]/30)
print("child num1: ",chi_1[0]/30," ",chi_1[1]/30," ",chi_1[2]/30)
print("child num2: ",chi_2[0]/30," ",chi_2[1]/30," ",chi_2[2]/30)
print("child num3: ",chi_3[0]/30," ",chi_3[1]/30," ",chi_3[2]/30)
print("child num4: ",chi_4[0]/30," ",chi_4[1]/30," ",chi_4[2]/30)

