# 

## 🎯 Objectif

  Compter le nombre de chaînes de longueur 'n' composées de voyelles, en suivant des règles spécifiques pour les transitions entre les voyelles.

---

## 📝 Détails

  Utilise la programmation dynamique pour optimiser le calcul.
  - 'a' suivi uniquement de 'e'
  - 'e' suivi de 'a' ou 'i'
  - 'i' ne peut pas être suivi de 'i'
  - 'o' suivi de 'i' ou 'u'
  - 'u' suivi uniquement de 'a'

---

## 📥 Entrée

  Un entier 'n' représentant la longueur de la chaîne.

---

## 📤 Sortie

  Un entier représentant le nombre de chaînes possibles modulo 10^9 + 7.

