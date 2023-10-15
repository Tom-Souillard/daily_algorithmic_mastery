# Encodeur Binaire Optimisé

## Description
Ce programme vise à optimiser l'encodage binaire d'un message donné en utilisant une méthode spécifique pour minimiser l'utilisation de 1 dans le binaire. Au lieu de simplement représenter le message en binaire, cette méthode le transforme en une série de blocs de zéros, chacun représentant une série de bits identiques (tous des 1 ou tous des 0).

## Fonctionnalités
- Convertit chaque caractère du message en sa représentation binaire ASCII (7 bits).
- Transforme la séquence binaire en une série de blocs de zéros.
- Chaque bloc est précédé par un indicateur : "0" pour une série de 1 et "00" pour une série de 0.
- La longueur du bloc indique le nombre de bits dans la série.

## Utilisation
L'utilisateur doit fournir :
- Le message à encoder.

Suite à cela, le programme affiche le message encodé selon la technique décrite.

## Entrée
- Message composé de caractères ASCII.

## Sortie
- Message encodé selon la technique d'optimisation.

## Contraintes
- 0 < N < 100, où N est la longueur du message.

## Remarque
Cette méthode d'encodage est particulièrement utile pour optimiser la transmission de données en minimisant le nombre de 1 transmis, ce qui peut avoir des avantages dans certains scénarios de communication.
