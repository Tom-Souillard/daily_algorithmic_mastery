# Calculateur de Résistance Équivalente

Le calculateur est conçu pour déterminer la résistance équivalente d'un circuit composé uniquement de résistances. Il prend en compte les configurations en série et en parallèle.

## Description

Le programme évalue les circuits électriques pour déterminer la résistance équivalente. Il se base sur des configurations en série et en parallèle :

1. **Série** : La résistance de résistances en série est égale à la somme de leurs résistances.
2. **Parallèle** : La résistance de résistances en parallèle est égale à l'inverse de la somme des inverses de leurs résistances.

## Utilisation

1. **Entrée** :
    - Un entier `N` représentant le nombre de résistances uniques dans le circuit.
    - Les `N` lignes suivantes contiennent un nom et une valeur de résistance.
    - La dernière ligne décrit la configuration du circuit à l'aide de parenthèses (pour les séries) et de crochets (pour les parallèles).

2. **Sortie** : 
    - La résistance équivalente du circuit sous forme de nombre flottant arrondi à 0,1 Ohms près.

## 📚 Bibliothèques Utilisées
    - `re` : Pour utiliser des expressions régulières lors de la manipulation de chaînes.

## ⚠️ Contraintes
- `0 < N < 10`
- `0 < R < 100`

