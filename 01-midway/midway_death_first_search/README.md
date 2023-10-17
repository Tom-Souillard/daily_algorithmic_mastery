# Death first search

## Objectif
Votre virus a infiltré le réseau Bobnet, ouvrant ainsi une backdoor qui vous permet d'envoyer de nouvelles instructions au virus en temps réel. Décidez d'attaquer activement en empêchant Bobnet de communiquer au sein de son réseau interne. Bobnet est divisé en sous-réseaux. Sur chaque sous-réseau, un agent Bobnet se déplace de noeud en noeud le long des liens pour atteindre une des passerelles menant vers un autre sous-réseau. Votre mission : reprogrammer le virus pour couper les liens et ainsi empêcher l'agent Bobnet de quitter son sous-réseau, l'empêchant d'informer le hub central de la présence de votre virus.

## Règles

### Description initiale
- Carte du sous-réseau.
- Emplacement des passerelles de sortie.
- Emplacement de départ de l'agent Bobnet.
- **Important :** Un noeud du réseau peut être lié à une seule passerelle au maximum.

### Déroulement du jeu
1. Coupez un lien du sous-réseau.
2. L'agent Bobnet se déplace vers un noeud accessible.

### Conditions de victoire
L'agent Bobnet ne peut atteindre aucune passerelle.

### Conditions de défaite
L'agent Bobnet atteint une passerelle.

## Entrées du jeu

### Initialisation
- `N`, `L`, `E` : Nombre de noeuds, liens et passerelles respectivement.
- `L` lignes suivantes : Liens entre les noeuds (N1, N2).
- `E` lignes suivantes : Index des passerelles.

### Boucle de jeu
- `SI` : Position de l'agent Bobnet (indice du nœud).

### Sortie pour un tour de jeu
- `C1` et `C2` : Indices des deux noeuds reliés par le lien à couper.
