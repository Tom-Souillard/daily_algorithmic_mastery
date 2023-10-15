# Simulateur de Chiffrement avec Rotors

Un outil de chiffrement qui utilise un décalage de type César, suivi d'une transformation via trois rotors.

## Utilisation

### Entrées

1. **Opération** : `ENCODE` pour chiffrer ou `DECODE` pour déchiffrer.
2. **Décalage initial** : Un chiffre entre 0 et 25.
3. **Rotors** : Trois configurations de rotors fournies ligne par ligne.
4. **Message** : La chaîne à traiter.

### Sortie

- Chaîne transformée selon l'opération et les paramètres fournis.

## Contraintes

- `0 ≤ Décalage < 26`
- Le message doit être constitué uniquement de lettres majuscules (A-Z).
- `1 ≤ longueur du message < 50`

