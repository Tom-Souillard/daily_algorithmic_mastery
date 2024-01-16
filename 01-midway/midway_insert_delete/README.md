# Insert Delete GetRandom O(1)

## 🎯 Objectif

  - Implémenter une classe `RandomizedSet` supportant l'insertion, la suppression et le renvoi aléatoire d'éléments avec une complexité temporelle moyenne de O(1).

---

## 📝 Détails

  - La classe utilise un dictionnaire pour mapper les valeurs à leurs indices dans un tableau.
  - Les opérations d'insertion et de suppression mettent à jour à la fois le dictionnaire et le tableau.

---

## 📥 Entrée

  - `insert(val: int)`: Insère la valeur `val` si elle n'est pas déjà présente.
  - `remove(val: int)`: Supprime la valeur `val` si elle est présente.
  - `getRandom()`: Renvoie un élément aléatoire du set.

---

## 📤 Sortie

  - `insert(val)`: Renvoie `True` si `val` a été inséré, `False` sinon.
  - `remove(val)`: Renvoie `True` si `val` a été supprimé, `False` sinon.
  - `getRandom()`: Renvoie un élément aléatoire du set.


