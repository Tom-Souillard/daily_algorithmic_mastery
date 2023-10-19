from typing import List, Optional

class Solution:
    def twoSum(self, nombres: List[int], cible: int) -> Optional[List[int]]:
        """Trouve deux indices de nombres dans la liste qui s'additionnent pour former la cible.

        Args:
            nombres (List[int]): Liste d'entiers à analyser.
            cible (int): Valeur cible pour la somme.

        Returns:
            Optional[List[int]]: Liste contenant les indices des deux nombres,
                                 ou None si aucune paire ne forme la cible.
        """
        table_hachage = {}

        for indice, nombre in enumerate(nombres):
            complement = cible - nombre

            if complement in table_hachage:
                return [table_hachage[complement], indice]

            table_hachage[nombre] = indice