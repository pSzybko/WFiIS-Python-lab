#1
#Proszę napisać iterator zwracający kolejne wyrazy ciągu Fibonacciego dwoma sposobami (jedna lub dwie klasy) i porównać ich wykorzystanie (2p).

class fibo:
  def __init__(self, max):
    self.max=max
    self.a=0
    self.b=1
  def __iter__(self):
    return self
  def __next__(self):
    val=self.a
    if self.a>self.max:
      raise StopIteration
    self.a=self.b
    self.b=val+self.b
    return val


t=fibo(10)
for i in t:
  print(f'{i}', end=' ')

class fibo2:
  def __init__(self, max):
    self.max=max
    self.a=0
    self.b=1
  def __iter__(self,):
    return fiboNext(self.max, self.a, self.b)

class fiboNext:
  def __init__(self, max, a, b):
    self.max=max
    self.a=a
    self.b=b
  def __next__(self):
    val=self.a
    if self.a>self.max:
      raise StopIteration
    self.a=self.b
    self.b=val+self.b
    return val
print()
t=fibo2(10)
for i in t:
  print(f'{i}', end=' ')

#2
#Proszę napisać iterator liczb pseudolosowych. Ciąg taki otrzymujemy ze wzoru:Xn+1 = (aXn + c) mod m, dla m = 231-1, a = 75, c = 0, x0 = 1.
#Korzystając z zaimplementowanego iteratora proszę wylosować 105 par liczb z przedziału [0,1). Proszę sprawdzić jaki procent wylosowanych par mieści się w kwadracie o boku 0.1*n, gdzie n∈[1,10]. Otrzymany wynik proszę porównać z wynikiem uzyskiwanym z wykorzystaniem generatora liczb pseudolosowych z języka Python (5p).
 
class pseudolos:
  def __init__(self, x, a, c, m, max):
    self.x=x
    self.a=a
    self.c=c
    self.m=m
    self.max=max
    self.l=0
  def __iter__(self):
    return self
  def __next__(self):
    self.l+=1
    if(self.l>self.max):
      raise StopIteration
    self.x=(self.x*self.a+self.c)%self.m
    return self.x/self.m

pl=pseudolos(1,7**5,0,2**31-1, 10)
print("\n")
for i in pl:
  print(i)
pl=pseudolos(1,7**5,0,2**31-1, 10**5)
ls=[]
for i in pl:
  ls.append(i)
perc=[0 for i in range(10)]
for i in range(len(ls)-1):
  perc[int(ls[i]*10)]+=1
for i in range(len(perc)):
  perc[i]/=10**3
print("nasz iterator:",perc)

import random
ls2=[random.random() for i in range (10**5)]
perc2=[0 for i in range(10)]
for i in range(len(ls2)-1):
  perc2[int(ls2[i]*10)]+=1
for i in range(len(perc2)):
  perc2[i]/=10**3
print("wbudowany:",perc2)


#3
#Proszę napisać iterator zwracający kolejne przybliżenie miejsca zerowego metodą Newtona-Raphsona: xn+1=xn-f(xn)/f'(xn) z zadaną dokładnością startując od określonej wartości początkowej, np. f(x)=sin(x)-(0.5x)2, x=1.5 i eps=10-5 (pochodna - scipy.misc) (3p).
from scipy import misc
from math import sin

class nr:
  def __init__(self, x, eps):
    self.x=x
    self.eps=eps
    

  def __iter__(self):
    return self
  def f(self, x):
    return sin(x)-(0.5*x)**2
  def __next__(self):
    tmp=self.x
    self.x=tmp-self.f(tmp)/misc.derivative(self.f, tmp)
    if abs(self.x-tmp)<self.eps:
      raise StopIteration
    return self.x

print()
newRaph=nr(1.5, 10**(-5))
for i in newRaph:
  print(i)

