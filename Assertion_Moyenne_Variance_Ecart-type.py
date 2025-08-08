L = [9, 10, 11, 20.5, 0, 12.0, -5, -8.3]
def rec_moy(L):
  L = []
  n=len(L)
  som = 0
  for i in range(n):
    som = som + L[i]
    moyenne = (1/n)*som
  return moyenne
  
def rec_variance(L):
  L = []
  n = len(L)
  somme = 0
  for i in range(n):
    somme = somme + L[i]**2
    variance = (1/n)*somme - rec_moy(L)**2
  return variance
from math import sqrt
def rec_ecart_type(L):
  return sqrt(rec_variance(L))

print("Moyenne de la liste :",rec_moy(L))
print("Variance de la liste :",rec_variance(L))
print("Ecart type de la liste :",rec_ecart_type(L))
