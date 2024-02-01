# Divide Array Into Arrays With Max Difference

## 🎯 Objectif

- Diviser un tableau en sous-tableaux de taille 3 avec une différence maximale entre éléments ≤ k.

---

## 📝 Détails

- Trier le tableau d'entrée.
- Itérer et regrouper les éléments par trois.
- Si la différence entre le plus grand et le plus petit élément d'un groupe est > k, retourner un tableau vide.

---

## 📥 Entrée

- `nums` : Liste[int] (le tableau d'entiers à diviser)
- `k` : int (la différence maximale autorisée)

---

## 📤 Sortie

- List[List[int]] contenant des sous-tableaux de taille 3 conformes à la condition, ou un tableau vide si impossible.


