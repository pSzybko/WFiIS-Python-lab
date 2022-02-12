#1

def generator1():
  n=0
  while True:
    yield n
    n+=1

def perfChecker(a):
  suma=sum([i for i in range (2,a) if not a%i], 1)
  return a==suma
  
def generator2(s):
  for i in s:
    if(perfChecker(i)):
      yield i

def generator3(s, n):
  for i in s:
    if(i>n):
      return 'blad'
    yield i

print(list(generator3(generator2(generator1()),100)))

#2
import math

def generator4():
  u,x=0.,1.
  a=0.05
  xi=x
  i=1
  while (xi<1.5):
    yield xi, u, math.log(xi)
    u=u+a/xi
    xi=x+i*a
    i+=1

for i in generator4():
  print(i)

#3
def generator5(x):
  l=[]
  for z in range(x):
    l.append(1)
  yield l
  while len(l)>2:
    l[len(l)-2]+=l[len(l)-1]
    l.pop(len(l)-1) 
    yield l
  while(l[0]<l[1]):
    l[0]+=1
    l[1]-=1
    yield l

for i in generator5(4):
  print(".",i)



#4
import random

def generator6():
  a=2
  while a>=0.1:
    yield a
    b=random.uniform(a, a+0.8)
    if(b>a+0.4):
      tmp=b-a
      b-=2*tmp
    a=b
print(list(generator6()))
#5

def myRange(start, stop=None, step=1.):
  start=float(start)
  if(step==0.):
    return 'blad'
  if(stop is None):
    stop=start
    start=0.
  while True:
    if (step>0 and start>=stop):
      break
    if (step<0 and start<=stop):
      break
    yield start
    start+=step

#range(8), range(-8), range(1,8), range(8,1), range(1,8,2), range(1,8,-2), range(8,1,2), range(8,1,-2)
for i in range(8,1,-2):
  print(i)

for i in myRange(8,1,-2):
  print(i)