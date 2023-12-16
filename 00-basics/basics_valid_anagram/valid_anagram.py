class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Determine if the second string is an anagram of the first string.

        An anagram is a word or phrase formed by rearranging the letters of a
        different word or phrase, typically using all the original letters exactly once.

        Args:
        s (str): The first string.
        t (str): The second string.

        Returns:
        bool: True if t is an anagram of s, False otherwise.
        """
        # Using a dictionary to count occurrences of each character in s and t
        compteur_s = {}
        compteur_t = {}

        # Count each character in s
        for caractere in s:
            if caractere in compteur_s:
                compteur_s[caractere] += 1
            else:
                compteur_s[caractere] = 1

        # Count each character in t
        for caractere in t:
            if caractere in compteur_t:
                compteur_t[caractere] += 1
            else:
                compteur_t[caractere] = 1

        # Compare the two dictionaries
        return compteur_s == compteur_t

# Testing the function
solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))  # Expected output: True
print(solution.isAnagram("rat", "car"))          # Expected output: False
