# Pseudo-Palindromic Paths in a Binary Tree

## 🎯 Objectif

- Compter les chemins pseudo-palindromiques dans un arbre binaire.

---

## 📝 Détails

- Un chemin est pseudo-palindromique si au moins une permutation des valeurs des nœuds est un palindrome.
- Utilisation d'une approche DFS (Depth-First Search) pour parcourir chaque chemin.
- Utilisation d'un bit mask pour suivre les comptes impairs/pairs des chiffres.

---

## 📥 Entrée

- root (Optional[TreeNode]): La racine de l'arbre binaire.

---

## 📤 Sortie

- int: Le nombre de chemins pseudo-palindromiques de la racine aux nœuds feuilles.


