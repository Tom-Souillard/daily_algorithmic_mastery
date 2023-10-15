# Résolution de formules d'une feuille de calcul 1D

## Objectif
L'outil traite une feuille de calcul unidimensionnelle pour résoudre ses formules et obtenir la valeur de chacune de ses cellules.

### Fonctionnement
Chaque cellule de la feuille de calcul est définie par une opération avec deux opérandes, `arg1` et `arg2`. Les opérations possibles sont :

- `VALUE arg1 arg2` : La valeur de la cellule est `arg1`. (`arg2` n'est pas utilisé).
- `ADD arg1 arg2` : La valeur de la cellule est `arg1 + arg2`.
- `SUB arg1 arg2` : La valeur de la cellule est `arg1 - arg2`.
- `MULT arg1 arg2` : La valeur de la cellule est `arg1 × arg2`.

Les opérandes peuvent être :

- Une référence (`$ref`) : Si un opérande commence par un signe dollar (`$`), il est interprété comme une référence à une autre cellule. La valeur de cette référence est égale à la valeur de la cellule référencée.
- Une valeur (`val`) : Si un opérande est un nombre, sa valeur est `val`.

### Entrée
- Ligne 1 : Un entier `N` représentant le nombre de cellules.
- Les `N` lignes suivantes : `operation arg1 arg2`.

### Sortie
- `N` lignes indiquant la valeur de chaque cellule, de la cellule 0 à la cellule `N`.

## Contraintes
- 1 ≤ `N` ≤ 100
- -10000 ≤ `val` ≤ 10000
- `$0` ≤ `$ref` ≤ `$(N-1)`
- `val` appartient aux entiers
- `ref` appartient aux nombres naturels
- Il n'y a pas de références cycliques.

## Implémentation
Le code utilise la récursion avec mise en cache (via `lru_cache` de `functools`) pour calculer la valeur de chaque cellule. La fonction `valeur` détermine la valeur d'une cellule en fonction de son opération et des valeurs ou références de ses opérandes.
