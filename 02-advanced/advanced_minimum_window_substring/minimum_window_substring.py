class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Finds the minimum window substring of s that contains all characters of t.

        Args:
        s: The string to search within.
        t: The string of characters to be included in the window.

        Returns:
        The minimum window substring that contains all characters of t. If no such
        substring exists, returns an empty string.
        """
        if not s or not t:
            return ""

        lettre_compte = {}
        for caractere in t:
            if caractere in lettre_compte:
                lettre_compte[caractere] += 1
            else:
                lettre_compte[caractere] = 1

        debut, fin = 0, 0
        debut_min, longueur_min = 0, float('inf')
        caracteres_restants = len(t)

        while fin < len(s):
            if s[fin] in lettre_compte:
                if lettre_compte[s[fin]] > 0:
                    caracteres_restants -= 1
                lettre_compte[s[fin]] -= 1

            while caracteres_restants == 0:
                if fin - debut + 1 < longueur_min:
                    debut_min, longueur_min = debut, fin - debut + 1

                if s[debut] in lettre_compte:
                    lettre_compte[s[debut]] += 1
                    if lettre_compte[s[debut]] > 0:
                        caracteres_restants += 1

                debut += 1

            fin += 1

        if longueur_min != float('inf'):
            return s[debut_min:debut_min + longueur_min]
        else:
            return ""
