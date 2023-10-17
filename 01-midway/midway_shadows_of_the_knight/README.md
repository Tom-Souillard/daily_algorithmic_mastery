# Shadows of the Knight

## Objectif

L'objectif de cet algorithme est de localiser une bombe dans un bâtiment en utilisant des indications de direction relatives à la position actuelle du détecteur. L'algorithme vise à atteindre la fenêtre où se trouve la bombe en un minimum de mouvements.

## Fonctionnement

1. **Initialisation** : 
    - Lire les dimensions `w` et `h` du bâtiment.
    - Lire le nombre maximal de mouvements autorisés `n`.
    - Lire la position initiale `x0`, `y0` du détecteur.

2. **Détermination de la zone de recherche** :
    - Initialement, la zone de recherche couvre tout le bâtiment. Cette zone est définie par quatre coordonnées : `xmin`, `xmax`, `ymin`, `ymax`.

3. **Boucle de recherche** : 
    - A chaque itération, lire la direction `bomb_dir` où se trouve la bombe par rapport à la position actuelle.
    - Mettre à jour les coordonnées de la zone de recherche en fonction de la direction `bomb_dir` :
        - Si `U` est dans `bomb_dir`, la bombe est au-dessus de la position actuelle, donc `ymax` est mis à jour à `y`.
        - Si `D` est dans `bomb_dir`, la bombe est en-dessous, donc `ymin` est mis à jour à `y`.
        - Si `R` est dans `bomb_dir`, la bombe est à droite, donc `xmin` est mis à jour à `x`.
        - Si `L` est dans `bomb_dir`, la bombe est à gauche, donc `xmax` est mis à jour à `x`.

4. **Mise à jour de la position** : 
    - Après avoir mis à jour la zone de recherche, calculer la nouvelle position `x`, `y` du détecteur comme le point central de cette zone.

5. **Sortie** : 
    - Afficher la nouvelle position `x`, `y` du détecteur.
