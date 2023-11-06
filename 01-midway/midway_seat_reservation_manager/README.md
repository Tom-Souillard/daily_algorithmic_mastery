# Seat Reservation Manager

## 🎯 Objectif

  - Gérer l'état des réservations de `n` sièges numérotés de 1 à `n`.

---

## 📝 Détails

  - Utilise un tas min (min-heap) pour optimiser les opérations de réservation et d'annulation.
  - Les sièges peuvent être réservés ou annulés de manière efficiente.

---

## 📥 Entrée

  - `__init__(n)`: un entier `n` représentant le nombre total de sièges.
  - `reserve()`: aucune entrée, réserve le siège disponible le plus petit.
  - `unreserve(seatNumber)`: l'entier `seatNumber` indiquant le numéro du siège à libérer.


---

## 📤 Sortie

  - `reserve()`: retourne un entier, le numéro du siège réservé.
  - `unreserve(seatNumber)`: ne retourne rien, le siège spécifié est remis disponible.


