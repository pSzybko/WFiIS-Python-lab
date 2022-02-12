from sys import argv

#1
if(len(argv)<2):
  print("Zle uruchomienie programu- proszę podać argumenty")
else:
  k=''.join(argv[1:])
  print(k)
  #2
  male=[i for i in k if i.islower()]
  duze=[i for i in k if i.isupper()]
  cyfry=[int(i) for i in k if i.isdigit()]
  nielitery=[i for i in k if i not in male and i not in duze]
  print(male)
  print(duze)
  print(cyfry)
  print(nielitery)
  #3
  mbp=[male[i] for i in range(len(male)) if male[i] not in male[:i]]
  print(mbp)
  lkmbp=[(i, male.count(i)) for i in mbp]
  print(lkmbp)
  #4
  lkmbp.sort(key=lambda x:x[1], reverse=True)
  print(lkmbp)
  #5
  samogloski=['a','e','i','u','o','y']
  a=0
  b=0
  for i in k:
    if i.lower() in samogloski:
      a+=1
  b=len(male)+len(duze)-a
  print(a,b) 

  def fkw(a,b,x):
    return a*x+b

  lkfkw=[(i,fkw(a,b,i)) for i in cyfry]
  print(lkfkw)  

  #6
  xsr=sum(i for i in cyfry)/len(cyfry)
  ysr=sum(fkw(a,b,i) for i in cyfry)/len(cyfry)
  #print(xsr,ysr)
  D=sum(((i-xsr)**2)for i in cyfry)
  #print(D)
  a1=(1/D)*sum(fkw(a,b,i)*(i-xsr) for i in cyfry)
  b1=ysr-a1*xsr
  print(a1,b1)
