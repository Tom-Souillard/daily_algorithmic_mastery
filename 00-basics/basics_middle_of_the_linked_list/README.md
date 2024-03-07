# 

## 🎯 Objectif

- Trouver et retourner le nœud du milieu d'une liste chaînée simplement. Pour une liste avec un nombre pair de nœuds, retourner le second nœud du milieu.

---

## 📝 Détails

- Utilisation de deux pointeurs, un rapide et un lent. Le pointeur rapide avance de deux nœuds à la fois, tandis que le lent avance d'un nœud.
- L'algorithme parcourt la liste en une seule passe, ce qui assure une complexité temporelle de O(n) et une complexité spatiale de O(1).

---

## 📥 Entrée

- head: Optional[ListNode] - La tête de la liste chaînée simplement.

---

## 📤 Sortie

- Optional[ListNode] - Le nœud du milieu de la liste.

