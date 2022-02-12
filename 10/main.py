#1
from datetime import date

def monthCalc(uro):
  if uro.year<1900 and uro.year>=1800:
    return 80
  if uro.year<2000 and uro.year>=1900:
    return 0
  if uro.year<2100 and uro.year>=2000:
    return 20
  if uro.year<2200 and uro.year>=2100:
    return 40
  if uro.year<2300 and uro.year>=2200:
    return 60

def f1(pesel, uro, plec):
  sumaKontrolna=[1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
  try:
    if uro.year%100!=int(pesel[0:2]):
      raise
    if uro.month + monthCalc(uro) != int(pesel[2:4]):
      raise
    if uro.day != int(pesel[4:6]):
      raise
    if plec=="f" and int(pesel[9])%2==1:
      raise
    if plec=="m" and int(pesel[9])%2==0:
      raise
    sum=0
    for i in range(len(sumaKontrolna)):
      sum+=int(pesel[i])*sumaKontrolna[i]
    sum%=10
    sum=10-sum
    sum%=10
    if sum!=int(pesel[10]):
      raise
    print("Poporawny pesel")
  except:
    print("Niepoprawny pesel")
f1("00232004759", date(2000,3,20), "m")

#2

#tryby r/l
def f2(plik, tryb="l"):
  wiek=0
  licz=1
  with open(plik, "r") as f:
    a=f.readlines()
    for i in a:
      tmp=i.split(" ")
      try:
        wiek+=date.today.year-int(tmp[1])
        licz+=1
        if len(tmp)!=3:
          raise Exception 
        
      except:
        print("Niepoprawna data")
        if(tryb=="r"):
          return 0
    return wiek/licz

print(f2("daty.in"))

#3
def f3(l):
  try:
    flaga=False
    if(len(l)<3):
      raise Exception
    for i in range(len(l)-2):
      if pow(l[i],2)+pow(l[i+1],2)==pow(l[i+2],2):
        even=0
        odd=0
        for j in range(3):
          if l[i+j]%2==0:
            even+=1
          else:
            odd+=1
        print("3 liczby tworzace trojke pitagorejska:", l[i], l[i+1], l[i+2], "gdzie parzytych liczb jest:",even, "a nieparzystych:", odd)
        flaga=True
    for i in range(len(l)-3):
      if pow(l[i],2)+pow(l[i+1],2)+pow(l[i+2],2)==pow(l[i+3], 2):
        even=0
        odd=0
        for j in range(4):
          if l[i+j]%2==0:
            even+=1
          else:
            odd+=1
        print("4 liczby tworzace czworke pitagorejska:", l[i], l[i+1], l[i+2],l[i+3], "gdzie parzytych liczb jest:",even, "a nieparzystych:", odd)
        flaga=True
    if flaga==False:
      raise
  except Exception as _:
    print("Niepoprawna dlugosc listy")
  except:
    print("brak trojek i czworek pitagorejskich")
l=(3,4)
f3(l)