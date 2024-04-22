# Open the Lock

## 🎯 Objectif

    Déterminer le nombre minimum de mouvements nécessaires pour atteindre une combinaison cible à partir de la combinaison initiale "0000" sur un cadenas à 4 roues, en évitant les combinaisons bloquées.

---

## 📝 Détails

    La fonction utilise une recherche en largeur bidirectionnelle pour optimiser l'exploration de l'espace des combinaisons possibles.

---

## 📥 Entrée

    deadends (List[str]) : Une liste de combinaisons qui bloquent le cadenas.
    target (str) : La combinaison cible que l'on cherche à atteindre.

---

## 📤 Sortie

    Un entier représentant le nombre minimal de mouvements nécessaires pour atteindre la combinaison cible, ou -1 si cela est impossible.

