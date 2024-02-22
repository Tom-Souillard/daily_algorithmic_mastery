# Find the Town Judge

## 🎯 Objectif

  Identifier l'étiquette du juge de la ville, si elle existe, en se basant sur les relations de confiance.

---

## 📝 Détails

  1. Le juge de la ville ne fait confiance à personne.
  2. Tout le monde (sauf le juge de la ville) fait confiance au juge.
  3. Il y a exactement une personne qui satisfait aux propriétés 1 et 2.

---

## 📥 Entrée

  1. n (int): Le nombre de personnes dans la ville.
  2. trust (List[List[int]]): Une liste de paires [a, b] représentant que la personne étiquetée a fait confiance à la personne étiquetée b.


---

## 📤 Sortie

  - L'étiquette du juge de la ville si elle existe, sinon -1.

