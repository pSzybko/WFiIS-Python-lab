#1
import time
import sys
import math
import random
import functools

powt=1000
N=10000
def forStatement():
  l=[]
  for i in range(N):
    l.append(i)
  return l

def listComprehension():
  return [i for i in range(N)]

def mapFunction():
  return map(lambda x: x, range(N))

def generatorExpression():
  return (i for i in range(N))

def tester(f):
  t=time.time_ns()
  for i in range(powt):
    f()
  t-=time.time_ns()
  return -t


''''
3.8.8 (default, Feb 20 2021, 21:09:14) 
[GCC 7.5.0]
forStatement         => 2719902271
listComprehension    => 1204514075
mapFunction          => 1221815
generatorExpression  => 1225894
'''
def forStatement():
  l=[]
  for i in range(N):
    l.append(i**2)
  return l

def listComprehension():
  return [i**2 for i in range(N)]

def mapFunction():
  return map(lambda x: x**2, range(N))

def generatorExpression():
  return (i**2 for i in range(N))


''''
3.8.8 (default, Feb 20 2021, 21:09:14) 
[GCC 7.5.0]
forStatement         => 7150584213
listComprehension    => 5567637226
mapFunction          => 1015277
generatorExpression  => 989319
'''
def tester(f):
  t=time.time_ns()
  suma=0
  for i in range(powt):
    for j in f():
      suma+=j
  t-=time.time_ns()
  return -t
''''
3.8.8 (default, Feb 20 2021, 21:09:14) 
[GCC 7.5.0]
forStatement         => 10318064137
listComprehension    => 9338428906
mapFunction          => 10095429011
generatorExpression  => 9457816407
'''

def tester(f):
  t=time.time_ns()
  suma=0
  for i in range(powt):
    suma+=sum(f())
  t-=time.time_ns()
  return -t

''''
3.8.8 (default, Feb 20 2021, 21:09:14) 
[GCC 7.5.0]
forStatement         => 8288800348
listComprehension    => 6391813737
mapFunction          => 7134607055
generatorExpression  => 5889282727
'''

def mapFunction():
  return list(map(lambda x: x, range(N)))

def generatorExpression():
  return list((i for i in range(N)))

def tester(f):
  t=time.time_ns()
  for i in range(powt):
    f()
  t-=time.time_ns()
  return -t

''''
3.8.8 (default, Feb 20 2021, 21:09:14) 
[GCC 7.5.0]
forStatement         => 7028774499
listComprehension    => 5838869656
mapFunction          => 1900440385
generatorExpression  => 1389347554

print(sys.version)
test=(forStatement, listComprehension, mapFunction, generatorExpression)

for testFunction in test:
    print(testFunction.__name__.ljust(20), '=>', tester(testFunction))
'''

#2
odl=[math.sqrt(random.uniform(-1,1)**2+random.uniform(-1,1)**2) for i in range(10000)]
pi=len(list(filter(lambda x: x<=1, odl)))*4/10000
print(pi)

#3
matrix=[[1,1,1,1],[1,2,3,4], [7,1,3,2], [6,1,12,0]]
matrix2=[[1,1,1,1],[1,2,3,4], [7,1,3,2], [6,1,12,0]]
print(list(map(max, matrix)))
print(list(map(max, zip(*matrix))))
print([list(map(sum, zip(*i))) for i in zip(matrix, matrix2)])

#4
def fun(l):
  return functools.reduce(lambda x,y: map(lambda x,y:[x,y] if not isinstance(x,list) else x+[y],x,y),l)
print(list(fun([[2,3],[4,5],[4,5],[1,2]]))) 