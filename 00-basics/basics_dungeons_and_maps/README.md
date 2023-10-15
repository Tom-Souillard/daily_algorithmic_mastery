# Chercheur de Trésor

## Description
Ce programme permet à un aventurier d'identifier parmi plusieurs cartes du donjon celle qui contient le chemin le plus court pour atteindre un trésor. Chaque carte est une représentation du même donjon, mais la position du trésor peut varier. Le programme est conçu pour éviter les pièges et les boucles infinies.

## Fonctionnalités
- Analyse des symboles des cartes pour déterminer les directions possibles.
- Suivi du chemin sur chaque carte en utilisant les indications fournies.
- Identification du chemin le plus court parmi toutes les cartes.
- Avertissement en cas de piège ou de boucle infinie sur une carte.

## Utilisation
L'utilisateur doit fournir les dimensions de la carte, la position de départ, le nombre total de cartes et les détails de chaque carte (représentant les chemins, les murs, les vides et le trésor).

## Entrée
- Dimensions de la carte (largeur et hauteur).
- Position de départ (ligne et colonne).
- Nombre de cartes.
- Détails de chaque carte, où chaque symbole représente:
  - `.` : Case vide.
  - `#` : Mur.
  - `^` : Déplacement vers le haut.
  - `v` : Déplacement vers le bas.
  - `<` : Déplacement vers la gauche.
  - `>` : Déplacement vers la droite.
  - `T` : Case du trésor.

## Sortie
- Index de la carte avec le chemin le plus court ou "TRAP" si aucun chemin valide n'a été trouvé.

## Contraintes
- Il y a toujours un trésor sur les cartes.
- Si plusieurs cartes contiennent un chemin valide, une seule contient le chemin le plus court.
- Les cartes fournies représentent le même donjon, mais la position du trésor peut différer.
- 0 < N < 10
- 2 < W, H < 20
