# Frequency of the Most Frequent Element

## 🎯 Objectif

  - Trouver la fréquence maximale d'un élément dans un tableau après au plus k opérations d'incrémentation.

---

## 📝 Détails

  - Utilise une approche de fenêtre glissante.
  - Trie le tableau et trouve la sous-séquence la plus longue où la somme des différences de tous les éléments au maximum dans cette fenêtre est ≤ k.
  - Complexité temporelle : O(n log n) ; Complexité spatiale : O(1).

---

## 📥 Entrée

  - `nums` (List[int]): Un tableau d'entiers.
  - `k` (int): Le nombre maximal d'opérations d'incrémentation autorisées.

---

## 📤 Sortie

  - int: La fréquence maximale possible d'un élément dans le tableau après avoir effectué les opérations.


