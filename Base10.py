n = 1234
def calcul_base10(n):
  L = []
  while n > 0:
    q = n // 10
    r = n % 10
    L.append(r)
    n = q
  L.reverse()
  return L

def somcube(n):
  som = 0
  for i in range(len(calcul_base10(n)):
    som = som + calcul_base10(n)**3
  return som

print("Calcul en base 10 :",calcul_base(n))
print("Somme des cube d'un entier :",somcube(n)) 
