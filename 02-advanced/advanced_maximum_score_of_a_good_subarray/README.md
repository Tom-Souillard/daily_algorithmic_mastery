# Maximum Score of a Good Subarray

## 🎯 Objectif

Calculer le score maximal d'un bon sous-tableau dans un tableau donné.

---

## 📝 Détails

- Un bon sous-tableau est un sous-tableau où i <= k <= j.
- Le score est défini comme min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1).


---

## 📥 Entrée

- nums (List[int]): Tableau d'entiers.
- k (int): Indice k à inclure dans le bon sous-tableau.


---

## 📤 Sortie

- int: Score maximal du bon sous-tableau.

