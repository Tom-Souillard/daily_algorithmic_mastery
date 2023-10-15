# Détecteur de défibrillateur le plus proche

## Description
Ce programme aide les utilisateurs à localiser le défibrillateur le plus proche en se basant sur leur position actuelle et une liste de défibrillateurs disponibles dans la ville de Montpellier.

## Fonctionnalités
- Conversion des coordonnées de degrés à radians.
- Calcul de la distance entre deux points en utilisant la formule de distance sur la surface d'une sphère.
- Comparaison des distances pour trouver le défibrillateur le plus proche.

## Utilisation
L'utilisateur fournit ses coordonnées (longitude et latitude) et le programme parcourt la liste des défibrillateurs disponibles pour identifier le plus proche.

## Entrée
- Longitude et latitude de l'utilisateur.
- Nombre total de défibrillateurs disponibles.
- Liste des défibrillateurs comprenant les détails suivants : Numéro d'identification, Nom, Adresse, Numéro de téléphone, Longitude, Latitude.

## Sortie
Le programme renvoie le nom du défibrillateur le plus proche de la position de l'utilisateur.

## Contraintes
- La liste des défibrillateurs ne doit pas dépasser 10 000.
- L'entrée et les coordonnées des défibrillateurs doivent être fournies en degrés, et elles sont ensuite converties en radians pour les calculs.
