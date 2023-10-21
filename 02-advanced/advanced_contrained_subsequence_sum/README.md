# Contrained Subsequence Sum

## 🎯 Objectif
  Trouver la somme maximale d'une sous-séquence non vide du tableau `nums` telle que pour chaque paire consécutive d'éléments, la condition `j - i <= k` est satisfaite.

---

## 📝 Détails

- Utilisation d'une deque pour maintenir une fenêtre glissante de la somme maximale dans un intervalle de taille `k`. Mise à jour des valeurs directement dans le tableau `nums` pour optimiser l'utilisation de la mémoire.

---

## 📥 Entrée

- Un tableau d'entiers `nums` et un entier `k`.

---

## 📤 Sortie

- Un entier représentant la somme maximale de la sous-séquence qui respecte la condition donnée.
