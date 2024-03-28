# Length of Longest Subarray With at Most K Frequency

## 🎯 Objectif

Trouver la longueur de la sous-séquence la plus longue dans laquelle la fréquence de chaque élément est inférieure ou égale à k.

---

## 📝 Détails

  - Utilise un approche de fenêtre glissante pour parcourir le tableau.
  - Garde le compte des fréquences des éléments dans la sous-séquence actuelle.
  - Ajuste la taille de la fenêtre pour maintenir la condition de "bonne" sous-séquence.

---

## 📥 Entrée

  - nums: List[int], un tableau d'entiers.
  - k: int, la fréquence maximale autorisée pour chaque élément dans une sous-séquence.

---

## 📤 Sortie

  - int, la longueur de la sous-séquence la plus longue répondant aux critères.

