class Solution:
    def customSortString(self, order: str, s: str) -> str:
        """
        Sorts the characters of the string `s` according to the custom order defined in the string `order`.

        Each character's relative order in `s` is rearranged to match the order they appear in `order`.
        Characters in `s` not present in `order` are appended at the end in their original order.

        Args:
        order (str): A string representing the custom order of characters.
        s (str): The string to be sorted based on the `order`.

        Returns:
        str: The permuted string `s` according to the custom order specified in `order`.

        Time Complexity: O(n + m) where n is the length of `s` and m is the length of `order`.
        Space Complexity: O(n) for storing the count and the output string, assuming the character set is fixed and does not contribute to space complexity.
        """
        # Compte le nombre d'occurrences de chaque caractère dans s
        compte = {}
        for caractere in s:
            if caractere in compte:
                compte[caractere] += 1
            else:
                compte[caractere] = 1

        # Construit la chaîne de sortie en suivant l'ordre personnalisé
        sortie = ""
        for caractere in order:
            if caractere in compte:
                sortie += caractere * compte[caractere]
                del compte[caractere]

        # Ajoute les caractères restants de s qui ne sont pas dans order
        for caractere, nombre in compte.items():
            sortie += caractere * nombre

        return sortie
