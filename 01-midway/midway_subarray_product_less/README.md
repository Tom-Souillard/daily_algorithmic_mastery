# Subarray Product Less Than K

## 🎯 Objectif

Calculer le nombre de sous-tableaux contigus dont le produit des éléments est strictement inférieur à k.

---

## 📝 Détails

Utilise une approche de fenêtre glissante pour parcourir le tableau, ajustant la taille de la fenêtre pour maintenir le produit des éléments sous le seuil k.

---

## 📥 Entrée

  - nums: List[int], un tableau d'entiers.
  - k: int, le seuil de produit.

---

## 📤 Sortie

int, le nombre total de sous-tableaux satisfaisant la condition.

