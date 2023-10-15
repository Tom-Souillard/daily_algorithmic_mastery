# Analyseur d'indexation d'array explicite

## Objectif
Ce programme a été créé pour mettre fin au débat entre l'indexation basée sur 0 et celle basée sur 1. Dans ce langage, il est nécessaire de préciser explicitement la plage d'indices qu'un tableau devrait avoir.

Vous recevez une liste de définitions de tableau, et votre tâche est de déterminer quel nombre est trouvé à un indice donné `i` d'un tableau `arr`. Il est à noter que les opérations d'indexation peuvent être imbriquées.

### Entrée
- Ligne 1 : Un entier `n` représentant le nombre de définitions de tableau.
- Les `n` lignes suivantes : Une définition de tableau par ligne.
- Ligne `n+2` : Élément à afficher sous la forme : `arr [ i ]`.

### Sortie
- Un entier unique correspondant à la valeur de l'indice recherché.

## Contraintes
- 1 <= `n` <= 100
- Chaque nom de tableau est composé uniquement de lettres majuscules (A à Z).
- Les longueurs des tableaux varient entre 1 et 100.
- Les opérations d'indexation ont au maximum 50 niveaux d'imbrication.
- Les indices sont toujours dans les limites dans les cas de test.

## Implémentation
Le code utilise les expressions régulières pour analyser chaque définition de tableau. La fonction `analyser_chaine` extrait le nom du tableau, les indices et les valeurs correspondantes. Une fois que tous les tableaux sont mémorisés, le programme résout l'opération d'indexation, même pour les opérations imbriquées, en utilisant la fonction `reduce` de `functools`.
