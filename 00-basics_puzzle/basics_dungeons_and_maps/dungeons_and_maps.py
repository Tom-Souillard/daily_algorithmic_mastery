dungeons_and_mapsimport sys
import math

# Lecture des dimensions de la carte et de la position de départ.
largeur, hauteur = [int(i) for i in input().split()]
ligne_depart, colonne_depart = [int(i) for i in input().split()]
nombre_cartes = int(input())

# Stockage des cartes dans la liste 'liste_cartes'.
liste_cartes = []
for i in range(nombre_cartes):
    carte = [list(input()) for j in range(hauteur)]
    liste_cartes.append(carte)


def suivre_chemin(carte, ligne_depart, colonne_depart):
    # Dictionnaire pour associer les directions aux mouvements.
    directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    ligne, colonne = ligne_depart, colonne_depart
    longueur_chemin = 0
    visite = set()

    while True:
        # Si la cellule a déjà été visitée, c'est une boucle. Retourner -1.
        if (ligne, colonne) in visite:
            return -1
        visite.add((ligne, colonne))

        # Si le trésor est trouvé, retourner la longueur du chemin.
        if carte[ligne][colonne] == 'T':
            return longueur_chemin
        # Si la cellule est vide ou un mur, c'est une impasse. Retourner -1.
        if carte[ligne][colonne] == '.' or carte[ligne][colonne] == '#':
            return -1
        # Se déplacer vers la prochaine cellule en suivant la direction de la cellule actuelle.
        deplacement_ligne, deplacement_colonne = directions[carte[ligne][colonne]]
        ligne += deplacement_ligne
        colonne += deplacement_colonne
        # Si le déplacement sort de la carte, retourner -1.
        if ligne < 0 or ligne >= hauteur or colonne < 0 or colonne >= largeur:
            return -1

        longueur_chemin += 1


# Trouver le chemin le plus court parmi toutes les cartes.
chemin_le_plus_court = float('inf')
carte_chemin_le_plus_court = -1

for i, carte in enumerate(liste_cartes):
    longueur_chemin = suivre_chemin(carte, ligne_depart, colonne_depart)
    if 0 < longueur_chemin < chemin_le_plus_court:
        chemin_le_plus_court = longueur_chemin
        carte_chemin_le_plus_court = i

# Afficher l'index de la carte avec le chemin le plus court ou "TRAP" si aucun chemin valide n'a été trouvé.
if carte_chemin_le_plus_court == -1:
    print("TRAP")
else:
    print(carte_chemin_le_plus_court)
