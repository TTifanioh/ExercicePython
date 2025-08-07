#coding:utf-8
from itertools import product

# Définir la fonction logique ici
def fonction_logique(A, B, C):
    return (A and not B) or C

# Obtenir les variables utilisées
variables = ['A', 'B', 'C']

# Générer toutes les combinaisons possibles des valeurs des variables
combinaisons = list(product([0, 1], repeat=len(variables)))

# Liste pour stocker les lignes de la table de vérité
table_verite = []

print("Table de vérité :")
print(" | ".join(variables) + " | F")
print("-" * (len(variables) * 4 + 5))

# Génération de la table de vérité
for ligne in combinaisons:
    valeurs = dict(zip(variables, ligne))
    resultat = fonction_logique(**valeurs)
    table_verite.append((ligne, int(resultat)))
    print(" | ".join(str(bit) for bit in ligne) + f" | {int(resultat)}")

# Construction de la première forme canonique (FDN)
fdn = []
for ligne, result in table_verite:
    if result == 1:
        terme = []
        for var, val in zip(variables, ligne):
            if val == 1:
                terme.append(var)
            else:
                terme.append(f"¬{var}")
        fdn.append("(" + " ∧ ".join(terme) + ")")

# Construction de la deuxième forme canonique (FCN)
fcn = []
for ligne, result in table_verite:
    if result == 0:
        terme = []
        for var, val in zip(variables, ligne):
            if val == 0:
                terme.append(var)
            else:
                terme.append(f"¬{var}")
        fcn.append("(" + " ∨ ".join(terme) + ")")

print("\nPremière forme canonique (FDN) :")
if fdn:
    print(" ∨ ".join(fdn))
else:
    print("Constamment 0")

print("\nDeuxième forme canonique (FCN) :")
if fcn:
    print(" ∧ ".join(fcn))
else:
    print("Constamment 1")
