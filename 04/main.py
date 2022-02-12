import random
import string
#1
print("\nzadanie 1\n")
k=int(10)
l=[random.randrange(0,5*k) for i in range(k)]
l2=l[:]
sl={i:0 for i in l}
print(l2)
print(l)
for i in range(100):
  random.shuffle(l)
  for j in range(k):
    if l2[j]==l[j]:
      sl[l[j]]+=1

print(l)
print(sl)
#2
print("\nzadanie 2\n")
s=""
s+='.'.join(random.choice(string.ascii_lowercase) for i in range(k))
print(s)

#3a
print("\nzadanie 3a\n")
l3=[random.randrange(0,20) for i in range (100)]
print(l3, '\n\n')
sl={}

for i,j in enumerate(l3):
  sl.setdefault(j,[]).append(i)
print(sl, '\n\n')
#3b
print("\nzadanie 3b\n")
sl2={}
k=0
for i in l3:
  sl2.setdefault(i,[]).append(l3.index(i, k))
  k=l3.index(i, k)+1
print(sl2, '\n\n')

#4
print("\nzadanie 4\n")
4000
def palindromchecker(x):
  xcpy=x
  tmp=0
  while x>0:
    k=x%10
    tmp*=10
    tmp+=k
    x=x//10
  return (xcpy==tmp)
print(palindromchecker(8008))
print(palindromchecker(13331))
licznik=0
for i in range (1000):
  if palindromchecker(random.randrange(100, 999999)):
    licznik+=1
print(licznik)
#5
print("\nzadanie 5\n")
sl3={i:random.randrange(1,100) for i in range(1,11)}
sl4={i:random.randrange(1,100) for i in range(1,11)}
print(sl3)
print(sl4, '\n')

sl3={i:j for j,i in sl3.items()}
sl4={i:j for j,i in sl4.items()}

print(sl3)
print(sl4, '\n')

sl5={i:(sl3[i], sl4[i]) for i in sl3 if i in sl4}

print(sl5)