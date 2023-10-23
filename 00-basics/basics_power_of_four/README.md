# Power of four 

## 🎯 Objectif

Déterminer si un entier donné est une puissance de 4.

---

## 📝 Détails

  - Utilisation d'opérations bit à bit pour vérifier si l'entier est une puissance de 2 (n & (n - 1) == 0).
  - Utilisation d'une constante hexadécimale (0xAAAAAAAA) pour vérifier si l'entier est une puissance de 4 (n & 0xAAAAAAAA == 0).


---

## 📥 Entrée

- Un entier n.

---

## 📤 Sortie

- Un booléen indiquant si n est une puissance de 4 ou non.
