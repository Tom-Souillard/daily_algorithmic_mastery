## Objectif

Le jeu se joue sur une grille rectangulaire de taille variable représentant une micro-puce. Certaines cellules de la grille contiennent des nœuds d'alimentation. Les autres cellules sont vides. Le but est d'indiquer, s'ils existent, le voisin horizontal et le voisin vertical de chaque nœud d'alimentation.

## Règles

Pour ce faire, vous devez trouver chaque nœud de coordonnées (x1,y1) et afficher les coordonnées (x2,y2) du premier nœud situé sur sa droite et les coordonnées (x3,y3) du premier nœud situé sous lui dans la grille. Si un voisin n'existe pas, vous devez afficher les coordonnées -1 -1 en lieu et place des coordonnées (x2,y2) et/ou (x3,y3).

Vous perdez si :

- Vous indiquez un voisin incorrect pour un nœud donné.
- Vous indiquez un voisin pour une cellule vide.
- Vous fournissez deux fois les voisins d'un nœud donné.
- Vous oubliez un nœud dans votre liste.

## Conditions de victoire

Vous gagnez la partie quand tous les voisins de tous les nœuds ont été affichés de manière correcte.

