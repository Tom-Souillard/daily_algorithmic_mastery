# Bus Routes

## 🎯 Objectif

- Trouver le nombre minimum de bus nécessaire pour voyager d'un arrêt de bus source à un arrêt de bus cible.

---

## 📝 Détails

- Utilisation de la recherche en largeur (BFS) pour explorer le réseau de bus.
- Création d'un graphique où chaque arrêt de bus est un nœud.
- Les nœuds sont connectés si un bus parcourt les deux arrêts.


---

## 📥 Entrée

- routes: Liste de listes, où chaque sous-liste représente une route de bus.
- source: L'arrêt de bus de départ.
- target: L'arrêt de bus de destination.


---

## 📤 Sortie

- Le nombre minimum de bus requis pour atteindre la cible depuis la source.
- Retourne -1 si le trajet n'est pas possible.


