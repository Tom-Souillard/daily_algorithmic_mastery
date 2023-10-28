class Solution:
    def countVowelPermutation(self, n: int) -> int:
        """
        Given an integer n, this function counts how many strings of length n can be formed under
        certain rules for transitioning between vowels.

        Args:
            n (int): The length of the string.

        Returns:
            int: The number of possible strings modulo 10^9 + 7.
        """
        MODULO = 10 ** 9 + 7  # Modulo constant
        dp_longueur = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}

        for _ in range(2, n + 1):
            nouveau_dp_longueur = {}

            nouveau_dp_longueur['a'] = dp_longueur['e']
            nouveau_dp_longueur['e'] = dp_longueur['a'] + dp_longueur['i']
            nouveau_dp_longueur['i'] = dp_longueur['a'] + dp_longueur['e'] + dp_longueur['o'] + dp_longueur['u']
            nouveau_dp_longueur['o'] = dp_longueur['i'] + dp_longueur['u']
            nouveau_dp_longueur['u'] = dp_longueur['a']

            for v in "aeiou":
                nouveau_dp_longueur[v] %= MODULO

            dp_longueur = nouveau_dp_longueur

        return sum(dp_longueur.values()) % MODULO
