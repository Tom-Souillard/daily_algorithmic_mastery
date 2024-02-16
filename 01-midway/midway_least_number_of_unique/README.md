# Least Number of Unique Integers after K Removals

## 🎯 Objectif

Trouver le nombre minimum d'entiers uniques après avoir supprimé k éléments de l'array.

---

## 📝 Détails

 - Utilisation d'un compteur pour comptabiliser la fréquence de chaque entier.
  - Tri des fréquences en ordre croissant.
  - Suppression des éléments basée sur leur fréquence jusqu'à atteindre ou dépasser k.

---

## 📥 Entrée

  - arr: List[int], un tableau d'entiers.
  - k: int, le nombre d'éléments à supprimer.

---

## 📤 Sortie

  - int, le nombre minimum d'entiers uniques restants après la suppression.

