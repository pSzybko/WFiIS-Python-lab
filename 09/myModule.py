from math import factorial

def trojPascala(n):
  for i in range(n):
    for j in range(n-i+1):
      print(end="   ")
    for j in range(i+1):
      print(factorial(i)//(factorial(j)*factorial(i-j)), end="      ")
    print()

def fun1(n,k):
  if(n<k or k==0):
    return 1
  if(k==n):
    return 0
  return (k+1)*fun1(n-1, k)+(n-k)*fun1(n-1, k-1)

def trojEulera(n):
  for i in range(n):
    for j in range(i):
      print(fun1(i,j), end=' '*(n-len(str(fun1(i,j)))))
    print()

def szyfrCezara(p, file1, file2):
  upperChange={(i, 65+(i+p-65)%26) for i in range(65, 91)}
  lowerChange={(i, 97+(i+p-97)%26) for i in range(97, 123)}
  change={}
  change.update(upperChange)
  change.update(lowerChange)

  with open(file1) as f1, open(file2, 'w') as f2:
    out=f1.readlines()
    for i in out:
      f2.write(i.translate(change))

def dekodSC(p, file1, file2):
  upperChange={(65+(i+p-65)%26, i) for i in range(65, 91)}
  lowerChange={(97+(i+p-97)%26, i) for i in range(97, 123)}
  change={}
  change.update(upperChange)
  change.update(lowerChange)

  with open(file1) as f1, open(file2, 'w') as f2:
    out=f1.readlines()
    for i in out:
      f2.write(i.translate(change))