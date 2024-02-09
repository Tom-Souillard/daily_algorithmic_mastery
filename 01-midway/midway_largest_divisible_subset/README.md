# Largest Divisible Subset

## 🎯 Objectif

- Trouver le plus grand sous-ensemble d'entiers positifs distincts où chaque paire d'éléments est mutuellement divisible.

---

## 📝 Détails

- Utilisation d'un algorithme de programmation dynamique pour optimiser la complexité spatiale et temporelle.
- Tri préalable de la liste pour faciliter la vérification de la divisibilité.
- Stockage de la taille du plus grand sous-ensemble et des indices précurseurs pour reconstruire le sous-ensemble.

---

## 📥 Entrée

- nums: List[int] - Une liste d'entiers positifs distincts.

---

## 📤 Sortie

- List[int] - Le plus grand sous-ensemble de 'nums' où pour toute paire (i, j), nums[i] % nums[j] == 0 ou nums[j] % nums[i] == 0.


