# Directional Path Finder

## Description
Ce projet est un algorithme de navigation qui guide un point (ou agent) sur une grille bidimensionnelle pour atteindre une cible.

## Caractéristiques 

- **Grille** : Dimensions configurables (exemple : 40x18).
- **Entrées** : 
  - Position initiale de l'agent.
  - Position de la cible.
- **Sorties** : Instructions séquentielles pour déplacer l'agent vers la cible.

## Instructions de Mouvement

L'agent peut se déplacer selon les directions suivantes :
- N (Nord)
- NE (Nord-Est)
- E (Est)
- SE (Sud-Est)
- S (Sud)
- SW (Sud-Ouest)
- W (Ouest)
- NW (Nord-Ouest)

Chaque mouvement déplace l'agent d'une case dans la direction choisie.

## Conditions

- **Victoire** : L'agent atteint la cible.
- **Défaite** : L'agent sort de la grille.

## Contraintes Techniques

- Les coordonnées X et Y doivent respecter les dimensions de la grille.
- Temps de réponse pour une instruction ≤ 100ms (modifiable selon les besoins).
