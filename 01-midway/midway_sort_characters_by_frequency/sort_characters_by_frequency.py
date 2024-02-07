class Solution:
    def frequencySort(self, s: str) -> str:
        """
        Sorts a string based on the frequency of its characters in decreasing order.

        Args:
        s: A string to be sorted based on character frequency.

        Returns:
        A string sorted by the frequency of its characters, with the most frequent characters first.

        The function first counts the frequency of each character in the input string using a dictionary.
        It then sorts the characters based on their frequencies in descending order. Finally, it constructs
        the sorted string by repeating each character by its frequency.
        """
        frequence = {}
        for caractere in s:
            if caractere in frequence:
                frequence[caractere] += 1
            else:
                frequence[caractere] = 1

        caracteres_tries = sorted(frequence, key=lambda x: frequence[x], reverse=True)

        resultat = ''.join([caractere * frequence[caractere] for caractere in caracteres_tries])

        return resultat
