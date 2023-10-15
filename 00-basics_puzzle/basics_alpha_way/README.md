# Traqueur de Séquence Alphabétique

## Description

Ce projet est conçu pour identifier et afficher une séquence consécutive de lettres allant de 'a' à 'z' dans une grille de caractères. La séquence peut se déplacer horizontalement (à gauche ou à droite) ou verticalement (vers le haut ou le bas) sur la grille.

## Fonctionnalité

À partir d'une grille donnée de taille `n x n`, le programme recherche la première lettre de la séquence, 'a', puis tente de suivre la séquence jusqu'à 'z'. Si une séquence valide est trouvée, elle est affichée, et tous les autres caractères sont remplacés par le symbole '-'. Si aucune séquence valide n'est trouvée, le programme ne retourne rien.

## Comment ça marche ?

Le cœur de ce programme repose sur une recherche en profondeur (DFS). À partir de chaque occurrence de 'a' trouvée dans la grille, le programme tente de suivre la séquence en explorant les possibilités dans toutes les directions jusqu'à ce qu'il atteigne 'z' ou se retrouve bloqué.

## Entrée

- Une ligne indiquant la taille de la grille `n`.
- `n` lignes représentant la grille, chaque ligne contenant `n` caractères alphabétiques en minuscule.

## Sortie

- Si une séquence valide est trouvée, la grille est affichée avec les lettres de la séquence et tous les autres caractères sont remplacés par '-'. Sinon, rien n'est retourné.

## Contraintes

- La grille est de taille `10<=n<=30`.
- La grille est composée uniquement de caractères alphabétiques minuscules.
- Il peut y avoir plusieurs occurrences de 'a'.
- Il n'y a qu'une seule séquence complète de 'a' à 'z' dans la grille.

## Code

Le programme est basé sur une fonction récursive `dfs` qui explore les possibilités à partir de chaque point et tente de construire la séquence requise.
