# Calculateur de Distance dans un Labyrinthe

Ce programme calcule le nombre minimal de mouvements nécessaires pour atteindre chaque cellule d'un point de départ dans un labyrinthe et visualise ces distances dans la configuration initiale du labyrinthe.

## Fonctionnalités

- **Traitement du Labyrinthe**: Analyse n'importe quel labyrinthe donné et calcule la distance à partir d'un point de départ désigné.
- **Gestion des Frontières Périodiques**: L'algorithme peut traiter des labyrinthes avec des frontières périodiques. Se déplacer au-delà d'un bord vous amène au bord opposé, sauf si un mur vous bloque.
- **Entrée Flexible**: Accepte une grande variété de configurations de labyrinthes avec des symboles personnalisables pour les points de départ, les murs et les espaces ouverts.
- **Visualisation des Distances**: Fournit une visualisation claire des distances à l'intérieur du labyrinthe à l'aide de caractères alphanumériques (0-9, A-Z).

## Utilisation

1. Définissez la configuration du labyrinthe avec les symboles appropriés.
2. Introduisez le labyrinthe dans le programme.
3. Obtenez un labyrinthe visualisé avec les distances à partir du point de départ.

## Contraintes

- La largeur et la hauteur du labyrinthe doivent être comprises entre 3 et 30.
- Il ne devrait pas y avoir plus de 35 mouvements nécessaires pour atteindre un point à l'intérieur du labyrinthe.

Pour des instructions d'utilisation plus spécifiques ou pour modifier les contraintes, reportez-vous à la documentation du code source.
