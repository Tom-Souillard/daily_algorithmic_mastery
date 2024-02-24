# Cheapest Flights Within K Stops

## 🎯 Objectif

Trouver le prix le moins cher pour un vol de src à dst avec au plus k escales.

---

## 📝 Détails

  - Il y a n villes connectées par certains vols.
  - Un vol est représenté par un tableau [from, to, price].

---

## 📥 Entrée

  - n (int): Le nombre total de villes.
  - flights (List[List[int]]): Liste des vols disponibles.
  - src (int): Ville de départ.
  - dst (int): Ville de destination.
  - k (int): Nombre maximal d'escales autorisées.

---

## 📤 Sortie

  - Le prix le moins cher pour atteindre dst depuis src avec au plus k escales. Retourner -1 si aucun chemin n'est trouvé.

