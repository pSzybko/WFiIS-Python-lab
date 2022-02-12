#1
#Proszę utworzyć klasę definiującą współrzędne punktu na płaszczyźnie. Obie współrzędne proszę zdefiniować jako własności (metoda inicjalizacyjna bezparametrowa) (1p)


class Point:
  def __init__(self):
    self.x=0
    self.y=0
  @property
  def x(self):
    return self._x
  @x.setter
  def x(self, nx):
    self._x=nx
  @x.getter
  def x(self):
    return self._x
  @property
  def y(self):
    return self._y
  @y.setter
  def y(self, ny):
    self._y=ny
  @y.getter
  def y(self):
    return self._y

test=Point()

print(test.x, test.y)
test.x=3
test.y=6
print(test.x, test.y)

#2
#Proszę zdefiniować funkcje dodawania i odejmowania współrzędnych (z wykorzystaniem wcześniej zdefiniowanej klasy) oraz opatrzyć je dekoratorem (implementowanym jako funkcja) sprawdzającym czy współrzędne leżą w określonym zakresie, jeżeli nie - proszę zgłosić wyjątek (3p)

def check(d, g):
  def fz(pf):
    def fw(w1, w2):
      if(w1.x<d or w2.x<d or w1.x>g or w2.x>g or w1.y<d or w2.y<d or w1.y>g or w2.y>g):
        raise
      return pf(w1, w2)
    return fw
  return fz

@check(-10, 10)
def dodaw(w1, w2):
  w=Point()
  w.x=w1.x+w2.x
  w.y=w1.y+w2.y
  return w

@check(-10,10)
def odejm(w1,w2):
  w=Point()
  w.x=w1.x-w2.x
  w.y=w1.y-w2.y
  return w

test2=Point()
test2.x=3
test2.y=7
print(test2.x, test2.y)
test3=dodaw(test, test2)
print(test3.x, test3.y)
test3=odejm(test, test2)
print(test3.x, test3.y)
#test2.x=67
#test3=odejm(test, test2)
#print(test3.x, test3.y)

#3
#Proszę utworzyć klasę z metodami statycznymi obliczającymi obwód i pole trójkąta lub czworokąta (dających się wpisać w okrąg, odpowiednio wzory Herona i Brahmagupty), zdefiniowanych poprzez współrzędne wierzchołków (klasa z zadania 1) (3p)

from math import sqrt

class pio:
  def __init__(self):
    pass
  @staticmethod
  def ot(w1, w2, w3):
    o=sqrt((w1.x-w2.x)**2+(w1.y-w2.y)**2)
    o+=sqrt((w1.x-w3.x)**2+(w1.y-w3.y)**2)
    o+=sqrt((w3.x-w2.x)**2+(w3.y-w2.y)**2)
    return o
  @staticmethod
  def oc(w1,w2,w3,w4):
    o=sqrt((w1.x-w2.x)**2+(w1.y-w2.y)**2)
    o+=sqrt((w2.x-w3.x)**2+(w2.y-w3.y)**2)
    o+=sqrt((w3.x-w4.x)**2+(w3.y-w4.y)**2)
    o+=sqrt((w4.x-w1.x)**2+(w4.y-w1.y)**2)
    return o
  @staticmethod
  def pt(w1,w2,w3):
    a=sqrt((w1.x-w2.x)**2+(w1.y-w2.y)**2)
    b=sqrt((w1.x-w3.x)**2+(w1.y-w3.y)**2)
    c=sqrt((w3.x-w2.x)**2+(w3.y-w2.y)**2)
    p=(a+b+c)/2
    return sqrt(p*(p-a)*(p-b)*(p-c))
  @staticmethod
  def pc(w1,w2,w3,w4):
    a=sqrt((w1.x-w2.x)**2+(w1.y-w2.y)**2)
    b=sqrt((w2.x-w3.x)**2+(w2.y-w3.y)**2)
    c=sqrt((w3.x-w4.x)**2+(w3.y-w4.y)**2)
    d=sqrt((w4.x-w1.x)**2+(w4.y-w1.y)**2)
    p=(a+b+c+d)/2
    return sqrt((p-a)*(p-b)*(p-c)*(p-d))

p1=Point()
p2=Point()
p3=Point()
p4=Point()

p1.x, p1.y = -1, -1
p2.x, p2.y = 1, -1
p3.x, p3.y = 1, 1
p4.x, p4.y = -1, 1

print(pio.oc(p1,p2,p3,p4))
print(pio.pc(p1,p2,p3,p4))

p1.x, p1.y = 0, 0
p2.x, p2.y = 2, 0
p3.x, p3.y = 0, 2

print(pio.ot(p1,p2,p3))
print(pio.pt(p1,p2,p3))

#4
#Proszę utworzyć dekorator (implementowany jako klasa) umożliwiający zliczenie liczby wywołań poszczególnych funkcji obłożonych dekoratorem, z metodą statyczną zwracającą wynik (3p)

class count:
  a={}
  def __init__(self, pf):
    self._pf=pf
    self._cnt=0
    count.a[pf]=self
  def __call__(self, p):
    self._cnt+=1
    return self._pf(p)
  @staticmethod
  def wynik():
    return {(f.__name__, count.a[f]._cnt) for f in count.a}

@count
def a(x):
  return 1

for _ in range(5):
  a(0)

print(count.wynik())