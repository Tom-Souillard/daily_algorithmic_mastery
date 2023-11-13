class Solution:
    def sortVowels(self, s: str) -> str:
        """
        Sort the vowels in the string 's' in nondecreasing ASCII order, while keeping consonants in their original places.

        Args:
        s (str): The input string containing vowels and consonants.

        Returns:
        str: The string after sorting vowels in nondecreasing ASCII order.

        The function first extracts all vowels from the input string and sorts them. Then, it iterates through the input string,
        replacing each vowel with the next sorted vowel in sequence.
        """

        # Identify vowels in both uppercase and lowercase.
        voyelles = set("aeiouAEIOU")

        # Extract vowels from the input string and sort them.
        voyelles_triees = sorted([caractere for caractere in s if caractere in voyelles])

        # Initialize an iterator for the sorted vowels.
        iterateur_voyelles = iter(voyelles_triees)

        # Replace vowels in the original string with sorted vowels.
        resultat = [next(iterateur_voyelles) if caractere in voyelles else caractere for caractere in s]

        # Return the resulting string.
        return ''.join(resultat)

# Example usage
sol = Solution()
print(sol.sortVowels("lEetcOde"))  # Output: "lEOtcede"
print(sol.sortVowels("lYmpH"))     # Output: "lYmpH"
