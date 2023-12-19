# Image Smoother

## 🎯 Objectif

  - Appliquer un filtre lissant 3x3 à chaque cellule d'une image en niveaux de gris.

---

## 📝 Détails

  - Le filtre calcule la moyenne de la cellule et des huit cellules environnantes.
  - Les cellules en bordure ou dans les coins sont traitées différemment.
  - La complexité spatiale et temporelle est optimisée.

---

## 📥 Entrée

  - `img` (List[List[int]]): Matrice 2D d'entiers représentant l'image en niveaux de gris.

---

## 📤 Sortie

  - Matrice 2D d'entiers représentant l'image lissée.


