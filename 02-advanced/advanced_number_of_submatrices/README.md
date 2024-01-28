# Number of Submatrices That Sum to Target

## 🎯 Objectif

- Calculer le nombre de sous-matrices non vides dont la somme est égale à une valeur cible donnée.

---

## 📝 Détails

- Utilise la somme préfixée et les hashmaps pour une optimisation de la complexité spatiale et temporelle.
- Itère sur toutes les paires de colonnes et calcule les sommes cumulatives pour chaque segment de ligne.

---

## 📥 Entrée

- matrix (List[List[int]]): Matrice d'entiers.
- target (int): Valeur cible pour la somme des sous-matrices.

---

## 📤 Sortie

- int: Nombre de sous-matrices dont la somme est égale à la valeur cible.


