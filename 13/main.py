#1
#Proszę napisać abstrakcyjną klasę Calka z metodą inicjalizacyjną określającą granice całkowania, liczbę kroków oraz funkcję podcałkową (proszę skontrolować poprawność przekazanych parametrów) oraz metodą abstrakcyjną obliczającą wartość całki.
#Następnie proszę utworzyć klasy dziedziczące po klasie Calka z metodami obliczającymi wartość całki odpowiednio metodą trapezów lub Simpsona, w metodzie proszę umieścić komentarz dokumentacyjny. Potrzebne wzory są w pliku: calki.pdf (3.(3)p)

import abc

class Calka(abc.ABC):
  def __init__(self, xp, xk, n, f):
    self.xp=xp
    self.xk=xk
    self.n=n
    self.f=f
  @abc.abstractmethod
  def oblicz(self):
    '''Metoda abstrakcyjna'''

class mTrapezow(Calka):
  def oblicz(self):
    self.h=(self.xk-self.xp)/self.n
    self.s=h/2*sum(self.f(i)+self.f(i+1) for i in range(1, self.n))
    return self.s

class mSimpsona(Calka):
  def oblicz(self):
    self.h=(self.xk-self.xp)/(2*self.n)
    self.s=h/3*(f(0)+4*sum(f(i) for i in range(1,2*self.n-1, 2))+2*sum(f(i) for i in range(2, 2*self.n-2, 2))+f(2*self.n))
    return self.s 


#2
#Proszę napisać klasę implementującą stos, klasa ma obsługiwać możliwość tworzenia pustego stosu bądź inicjalizacji istniejącym stosem (obiektem klasy), dodawania i usuwania elementu, dodawania elementów innego stosu, zwracania rozmiaru i wypisywania stosu.

class stos:
  def __init__(self, other=None):
    if(other is not None):
      self.data=[e for e in other.data]
    else:
      self.data=[]
  def push(self, e):
    self.data.append(e)
  def pop(self):
    self.data.pop()
  def pushS(self, other):
    for e in other.data:
      self.data.append(e)
  def __len__(self):
    return len(self.data)
  def __str__(self):
    wyn=' '
    wyn.join(self.data)
    return wyn

#Następnie proszę napisać klasę dziedziczącą po klasie stosu i implementującą stos posortowany (rosnąco lub malejąco). W tym przypadku element/elementy innego stosu można do stosu dodać pod warunkiem zachowania porządku sortowania.

class sortedStos(stos):
  def __init__(self, other=None):
    if(other is not None and other==other.sort()):
      self.data=[e for e in other.data]
    else:
      self.data=[]
  def push(self, e):
    if(len(self)==0 or self.data[-1]<e):
      self.data.append(e)
  def pushS(self, other):
    if(len(self)==0 or self.data[-1]<other.data[0]):
      for e in other.data:
        self.data.append(e)
  

#Proszę sprawdzić jaki jest średni rozmiar posortowanego stosu, który wypełniamy całkowitymi liczbami losowymi z przedziału [0,100] losując 100 wartości (średnia po 100 powtórzeniach) (3.(3)p)

from random import randint

srednia=0

for _ in range(100):
  ss=sortedStos()
  for _ in range(100):
    ss.push(randint(0, 100))
  srednia+=len(ss)

print(srednia/100)

#3
#Proszę zaimplementować klasę pozwalającą na zliczanie linii, słów i znaków w pliku (metody inicjalizująca i zliczająca). W klasie proszę także zaimplementować bezparametrową metodę statyczną zwracają komunikat analogiczny do komunikatu zwracanego przez polecenie systemowe linuxa wc w przypadku jednoczesnego zliczania dla kilku plików (3.(3)p)

class countLSZ:
  l=0
  s=0
  z=0
  def __init__(self, *files):
    self.f=[]
    self.lp=0
    self.sp=0
    self.zp=0
    for e in files:
      self.f.append(e)
  @staticmethod
  def printAll():
    print(countLSZ.l, countLSZ.s, countLSZ.z, "RAZEM")
  def zlicz(self):
    for e in self.f:
      with open(e, 'r') as file:
        self.lp=0
        self.sp=0
        self.zp=0
        for line in file:
          self.zp+=len(line)
          self.lp+=1
          slowa=line.split()
          self.sp+=len(slowa)
        countLSZ.l+=self.lp
        countLSZ.s+=self.sp
        countLSZ.z+=self.zp
      print(self.lp, self.sp, self.zp, e)
    countLSZ.printAll()
  

test=countLSZ("a.txt", "b.txt")
test.zlicz()
