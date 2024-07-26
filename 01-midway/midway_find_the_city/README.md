# Find the City With the Smallest Number of Neighbors at a Threshold Distance

## 🎯 Objectif

    Trouver la ville avec le plus petit nombre de voisins à une distance donnée.

---

## 📝 Détails

    Utiliser l'algorithme de Floyd-Warshall pour calculer les plus courtes distances entre chaque paire de villes.
    Parcourir chaque ville et compter le nombre de villes accessibles dans le seuil de distance.

---

## 📥 Entrée

    Le nombre de villes n.
    Une liste d'arêtes où chaque arête est représentée par [from, to, weight].
    Un seuil de distance.

---

## 📤 Sortie

La ville avec le plus petit nombre de voisins dans le seuil de distance. En cas d'égalité, retourner la ville avec le plus grand numéro.

