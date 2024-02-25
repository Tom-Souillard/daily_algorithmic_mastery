# Greatest Common Divisor Traversal

## 🎯 Objectif

- Déterminer s'il est possible de parcourir entre toutes les paires d'indices dans un tableau donné, en utilisant le critère que le PGCD (plus grand commun diviseur) des valeurs aux indices i et j est supérieur à 1.

---

## 📝 Détails

- Utilisation de l'algorithme Union-Find pour grouper les éléments qui partagent un facteur premier commun.
- Identification des facteurs premiers pour chaque élément et création de connexions entre les indices partageant un même facteur premier.
- Vérification si tous les éléments sont connectés à un seul composant, indiquant la possibilité d'un parcours entre chaque paire d'indices.

---

## 📥 Entrée

- nums: Liste d'entiers représentant le tableau à parcourir.

---

## 📤 Sortie

- Un booléen indiquant s'il est possible de parcourir entre toutes les paires d'indices sous la condition donnée.

