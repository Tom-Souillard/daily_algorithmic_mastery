from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        """
        Play tokens to maximize score within the given power limit. You can play a token face up to gain score if you have enough power, or play it face down to gain power if you have at least 1 score.

        Args:
        tokens (List[int]): The values of tokens.
        power (int): Initial power.

        Returns:
        int: The maximum score achievable.
        """
        tokens.sort()  # Tri des jetons par ordre croissant
        score = 0  # Score initial
        max_score = 0  # Score maximal atteignable
        debut = 0  # Index du début de la liste des jetons
        fin = len(tokens) - 1  # Index de fin de la liste des jetons

        while debut <= fin:
            if power >= tokens[debut]:  # Si assez de puissance pour jouer le jeton face visible
                power -= tokens[debut]  # Joue le jeton face visible, perd de la puissance
                score += 1  # Gagne 1 score
                max_score = max(max_score, score)  # Mise à jour du score maximal
                debut += 1  # Avance au prochain jeton
            elif score > 0:  # Si pas assez de puissance mais au moins 1 score pour jouer face cachée
                power += tokens[fin]  # Joue le jeton face cachée, gagne de la puissance
                score -= 1  # Perd 1 score
                fin -= 1  # Recule au jeton précédent
            else:  # Si impossible de jouer le jeton
                break  # Arrête la boucle

        return max_score
