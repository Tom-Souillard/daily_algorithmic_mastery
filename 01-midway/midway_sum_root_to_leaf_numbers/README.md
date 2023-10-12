# Sum Root to Leaf Numbers

## 🎯 Objectif

Calculer la somme de tous les nombres représentés par les chemins de la racine jusqu'aux feuilles dans un arbre binaire.


---

## 📝 Détails

Utiliser un parcours en profondeur (DFS) pour explorer chaque chemin de la racine aux feuilles. Chaque noeud contribue à former un nombre en ajoutant sa valeur au nombre formé par ses ancêtres.


---

## 📥 Entrée

Un arbre binaire où chaque noeud contient un chiffre de 0 à 9.

---

## 📤 Sortie

Un entier représentant la somme totale des nombres formés par tous les chemins de la racine aux feuilles.