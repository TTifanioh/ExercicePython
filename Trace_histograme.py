L=[2, 2, 6, 6, 3, 14, 14, 6, 8, 9, 9]
import matplotlib.piplot as plt
plt.figure()
plt.hist(L, bins=1é, color='red')
plt.title("Histogramme de la liste L")
plt.xlabel("Valeurs de L")
plt.ylabel("Nombre d'occurrences")
plt.show()
