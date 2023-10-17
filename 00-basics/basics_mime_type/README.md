# Détecteur de type MIME

## Objectif
Le but de ce programme est de déduire le type MIME d'un fichier basé sur son nom. Le type MIME est largement utilisé pour identifier le type de contenu dans les protocoles Internet.

## Règles
Une table associant une extension de fichier à un type MIME est fournie. À partir de cette table, le programme devra déterminer le type MIME pour une liste donnée de noms de fichiers.

L'extension d'un fichier est définie comme la partie du nom qui suit le dernier point. Si l'extension est trouvée dans la table, le programme affiche le type MIME correspondant. Sinon, il affiche "UNKNOWN".

## Entrées et Sorties

### Entrées
- Ligne 1 : Un entier `N` indiquant le nombre d'entrées dans la table d'association.
- Ligne 2 : Un entier `Q` représentant le nombre de noms de fichiers à analyser.
- `N` lignes suivantes : Chaque ligne contient une extension suivie de son type MIME correspondant.
- `Q` lignes suivantes : Chaque ligne contient un nom de fichier à analyser.

### Sorties
Pour chaque nom de fichier fourni, le programme affiche le type MIME associé ou "UNKNOWN" s'il n'y a pas de correspondance.

## Contraintes
- 0 < N < 10000
- 0 < Q < 10000
- Les extensions contiennent jusqu'à 10 caractères ascii alphanumériques.
- Les types MIME contiennent jusqu'à 50 caractères ascii alphanumériques et de ponctuation.
- Les noms de fichiers contiennent jusqu'à 256 caractères ascii alphanumériques et des points.
- Il n'y a pas d'espaces dans les noms de fichiers, les extensions et les types MIME.

## Fonctionnement
Le programme commence par lire la table d'association et stocke les correspondances dans un dictionnaire. Ensuite, pour chaque nom de fichier, il déduit son extension, recherche l'extension dans le dictionnaire et affiche le type MIME associé ou "UNKNOWN" si aucune correspondance n'est trouvée.
``
