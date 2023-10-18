import sys


# Définition de la classe Usine pour stocker les informations sur chaque usine
class Usine:
    def __init__(self, identifiant, proprietaire, cyborgs, production):
        self.identifiant = identifiant
        self.proprietaire = proprietaire
        self.cyborgs = cyborgs
        self.production = production


# Fonction pour décider de la cible à attaquer en fonction de différents critères
def choisir_cible(liste_usines, distances, usine_source):
    meilleur_score = -float('inf')
    meilleure_cible = None

    # Parcourir toutes les usines pour décider quelle usine attaquer
    for id_cible, usine_cible in liste_usines.items():
        if id_cible == usine_source.identifiant or usine_cible.proprietaire == 1:
            continue
        distance = distances[usine_source.identifiant][id_cible]
        score = usine_cible.production - distance - usine_cible.cyborgs  # calcul d'un score simple

        if score > meilleur_score:
            meilleur_score = score
            meilleure_cible = usine_cible
    return meilleure_cible


# Initialisation des variables
liste_usines = {}
distances_entre_usines = {}
# Lecture des données initiales
nombre_usines = int(input())
nombre_liens = int(input())
print(f"nombre_usines = {nombre_usines}, nombre_liens = {nombre_liens} ", file=sys.stderr, flush=True)
# Initialisation de la matrice des distances
for i in range(nombre_usines):
    distances_entre_usines[i] = {}
    for j in range(nombre_usines):
        distances_entre_usines[i][j] = float('inf')
print(f"intialisation matrice des distance : {distances_entre_usines}", file=sys.stderr, flush=True)
# Lecture des distances entre les usines
for i in range(nombre_liens):
    usine_1, usine_2, distance = map(int, input().split())
    distances_entre_usines[usine_1][usine_2] = distance
    distances_entre_usines[usine_2][usine_1] = distance

    print(f"lien {i}", file=sys.stderr, flush=True)
    print(f"distances_entre_usines[{usine_1}][{usine_2}] = {distances_entre_usines[usine_1][usine_2]}", file=sys.stderr,
          flush=True)
    print(f"distances_entre_usines[{usine_2}][{usine_1}] = {distances_entre_usines[usine_2][usine_1]}", file=sys.stderr,
          flush=True)
print(f"distances_entre_usines = {distances_entre_usines}", file=sys.stderr, flush=True)
# Boucle de jeu
while True:
    nombre_entites = int(input())
    print(f"nombre_entites = {nombre_entites}", file=sys.stderr, flush=True)
    # Réinitialisation des structures de données
    liste_usines.clear()

    # Lecture des entités (usines et troupes)
    for i in range(nombre_entites):
        donnees = input().split()
        id_entite = int(donnees[0])
        type_entite = donnees[1]
        # Lecture des données de l'usine
        if type_entite == 'FACTORY':
            proprietaire = int(donnees[2])
            cyborgs = int(donnees[3])
            production = int(donnees[4])
            liste_usines[id_entite] = Usine(id_entite, proprietaire, cyborgs, production)
    # Stratégie : Décider des cibles en fonction de la priorité
    ordres = []
    for id_usine, usine in liste_usines.items():
        if usine.proprietaire == 1:  # Mes usines

            # Décider de l'usine cible à attaquer ou à renforcer
            cible = choisir_cible(liste_usines, distances_entre_usines, usine)
            if cible:
                cyborgs_necessaires = cible.cyborgs + 1
                if usine.cyborgs > cyborgs_necessaires:
                    ordres.append(f"MOVE {id_usine} {cible.identifiant} {cyborgs_necessaires}")
    if not ordres:
        print("WAIT")
    else:
        print(";".join(ordres))
