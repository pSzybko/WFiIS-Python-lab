#1
#metodę inicjalizującą przyjmującą jako parametr współczynniki przekształcenia oraz prawdopodobieństwa i określającą początkowe współrzędne punktu jako (0,0),
import random
class IFS:
  def __init__(self, wsp, praw):
    self.x=0
    self.y=0
    self.arrx=[]
    self.arry=[]
    self.arrwsp=wsp
    self.arrpraw=praw
  
  def nowewsp(self, t):
    for _ in range (t):
      arrwsp=random.choices(self.arrwsp, self.arrpraw)
      self.x=arrwsp[0]*self.arrx[-1]+arrwsp[1]*self.arrx[-1]+arrwsp[2]
      self.y=arrwsp[3]*self.arrx[-1]+arrwsp[4]*self.arrx[-1]+arrwsp[5]
      self.arrx.append(self.x)
      self.arry.append(self.y)
    
#2
#przeciążające operatory dodawania, odejmowania, mnożenia (mnożenie wektora przez liczbę) oraz metodę str
from math import pow
class Wektor:
  def __init__(self, *l):
    self.arr=[]
    for i in l:
      self.arr.append(i)

  def __str__(self):
    s=''
    for i in self.arr:
      s+=str(i)
      s+=" "
    return s

  def __add__(self, other):
    if( len(self.arr)==len(other.arr)):
      wynik=Wektor()
      for i in range(len(self.arr)):
        wynik.arr.append(self.arr[i]+other.arr[i])
      return wynik

  def __sub__(self, other):
    if( len(self.arr)==len(other.arr)):
      wynik=Wektor()
      for i in range(len(self.arr)):
        wynik.arr.append(self.arr[i]-other.arr[i])
      return wynik
  def __mul__(self, n):
    wynik=Wektor()
    for i in self.arr:
      wynik.arr.append(n*i)
    return wynik
  def len(self):
    return pow(sum(pow(x,2) for x in self.arr),0.5)
  def ilskal(self, other):
    if(len(self.arr)==len(other.arr)):
      return sum(self.arr[x]*other.arr[x] for x in range(len(self.arr)))
  def ilwekt(self, other):
    wynik=Wektor()
    if len(self.arr)==len(other.arr)==3:
      for i in range(3):
        if i==0:
          wynik.arr.append(self.arr[1]*other.arr[2]-self.arr[2]*other.arr[1])
        elif i==1:
          wynik.arr.append(self.arr[2]*other.arr[0]-self.arr[0]*other.arr[2])
        else:
          wynik.arr.append(self.arr[0]*other.arr[1]-self.arr[1]*other.arr[0])
      return wynik
  def ilmiesz(self, other1, other2):
    return self.ilskal(other1.ilwekt(other2))

        

w1=Wektor(1,2,3)
w2=Wektor(0,1,0)
w3=w1+w2
w4=w1-w2
w5=w1*5
print(w3)
print(w4)
print(w1.len())
print(w1)
print(w2)
w1=Wektor(2,4,6)
w2=Wektor(6,3,2)
w3=Wektor(4,9,4)
print(w1.ilmiesz(w2, w3))


#3
def sim(B, S):
  return B.ilskal(S)

def FLorentza(q, E, v, B):
  return q*(E+v.ilwekt(B))

def WFLorentza(q, E, v):
  return q*E.ilskal(v)
