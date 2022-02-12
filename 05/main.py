from sys import argv
import random
import string

#1
def fun1(str):
  s=''.join(i for i in str if i in string.ascii_lowercase)
  s2=''.join(random.SystemRandom().choice(string.digits) for _ in range(len(s)))
  sl=str.maketrans(s,s2)
  sl[120]=120
  str=str.translate(sl)
  print(str)
  l=[random.random() for _ in range(10)]
  l2=[(x, eval(str)) for x in l]
  return l2

print(fun1('a*x**2+b*x+c'))
#2
def fun2(*x):
  lista=[]
  for i in x[0]:
    for j in x[1:]:
      if i not in j:
        break
    else:
      lista.append(i)
  return lista

print(fun2([1,2,3],(1,3,5), [3,2,1]))
print(fun2([1,2,3],(1,3,5), [3,2]))

#3

def fun3(a,b,c=True):
  if c:
    return [(a[i], b[i]) for i in range(min(len(a),len(b)))]
  else:
    return [(a[i], b[i]) if i<min(len(a), len(b)) else (None, b[i]) if len(a)<len(b) else (a[i], None) for i in range (max(len(a), len(b)))]

print(fun3([1,2,3,4,5,], [2,7,4], False))
print(fun3([1,2,3,4,5,], [2,7,4]))

#4

def fun4(k, n=(10,5,2)):
  m=[]
  while k>min(n):
    for i in n:
      while k>=i:
        m.append(i)
        k-=i
  print(m, end='')
  if k!=0:
    print(" reszta: ", k)
  print()

fun4(17)
fun4(17, (5,2))
fun4(17, (2,))

#5

def fun5(x,d,g,z='r'):
  kroki=0
  p=True
  while p:
    if z=='r':
        p=False if random.randrange(d,g)==x else True    
    else: 
      y=d+(g-d)//2
      z=[i for i in range(d, y)]
      z=[i for i in range(d, y)] if x in z else [i for i in range(y, g)]
      p=False if x==random.randrange(z[0], z[-1]) else True
    kroki+=1
  return kroki
  
print(fun5(13,0,27,1))
print(fun5(13,0,27))
