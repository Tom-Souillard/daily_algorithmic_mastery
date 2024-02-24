# Find All People With Secret

## 🎯 Objectif

Retourner une liste de toutes les personnes qui connaissent le secret après toutes les réunions.

---

## 📝 Détails

  - Les secrets sont partagés instantanément durant les réunions.
  - Une personne peut assister à plusieurs réunions au même moment.
  - Le partage initial du secret est entre la personne 0 et une personne donnée (firstPerson) à l'instant 0.

---

## 📥 Entrée

  - n: un entier représentant le nombre de personnes (numérotées de 0 à n - 1).
  - meetings: un tableau 2D d'entiers où meetings[i] = [xi, yi, timei] représente une réunion entre les personnes xi et yi à l'instant timei.
  - firstPerson: un entier représentant la personne avec laquelle le secret est initialement partagé.

---

## 📤 Sortie

Une liste d'entiers représentant toutes les personnes qui connaissent le secret, dans n'importe quel ordre.

