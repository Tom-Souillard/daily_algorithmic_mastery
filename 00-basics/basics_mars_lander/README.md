# Atterrissage de "Mars Lander"

## Objectif
L'objectif de cet algorithme est d'assurer un atterrissage sûr et contrôlé de la capsule "Mars Lander" qui transporte le rover Opportunity sur la surface de Mars.

## Règles
- Le simulateur initialise la capsule dans une zone spécifique du ciel martien.
- La zone a des dimensions de 7000m x 3000m.
- Mars Lander commence au-dessus de la zone d'atterrissage avec une vitesse initiale nulle et en position verticale.
- La zone d'atterrissage est plane et a une largeur d'au moins 1000 mètres.
- Toutes les secondes, le programme doit donner les instructions pour le nouvel angle de rotation et la puissance des fusées.
  - Angle entre -90° et 90°.
  - Puissance des fusées entre 0 et 4.
- Pour réussir l'atterrissage :
  - Atterrir sur un sol plat.
  - La position doit être verticale (angle = 0°).
  - Vitesse verticale ≤ 40 m/s.
  - Vitesse horizontale ≤ 20 m/s.
- Remarques pour simplifier :
  - La zone d'atterrissage est juste en dessous du robot.
  - Seule la vitesse d'atterrissage est importante, entre 0 et 40m/s.

## Entrées
### Initialisation
- **surfaceN** : Nombre de points formant le sol de Mars.
- **landX, landY** : Coordonnées de ces points.

### Pour un tour de jeu
- **X, Y** : Coordonnées de Mars Lander.
- **hSpeed, vSpeed** : Vitesses horizontales et verticales.
- **fuel** : Quantité de fuel restante.
- **rotate** : Angle de rotation actuel.
- **power** : Puissance actuelle des fusées.

## Sortie
Pour chaque tour :
- **rotate** : Angle de rotation souhaité.
- **power** : Puissance des fusées souhaitée.

## Contraintes
- 2 ≤ surfaceN < 30
- 0 ≤ X < 7000
- 0 ≤ Y < 3000
- -500 < hSpeed, vSpeed < 500
- 0 ≤ fuel ≤ 2000
- -90 ≤ rotate ≤ 90
- 0 ≤ power ≤ 4
- Temps de réponse pour un tour ≤ 100ms
