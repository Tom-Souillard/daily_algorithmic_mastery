class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Given a string of digits 2-9, returns all possible letter combinations the digits could represent on a telephone keypad.

        Args:
        digits: A string containing digits from 2-9.

        Returns:
        A list of strings representing all possible letter combinations.
        """
        if not digits:
            return []

        mapping = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        def backtrack(index, path):
            if index == len(digits):
                combinaisons.append("".join(path))
                return

            for lettre in mapping[digits[index]]:
                path.append(lettre)
                backtrack(index + 1, path)
                path.pop()

        combinaisons = []
        backtrack(0, [])
        return combinaisons


# Partie test
if __name__ == "__main__":
    solution = Solution()
    # Test 1
    print(solution.letterCombinations("23"))  # ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    # Test 2
    print(solution.letterCombinations(""))  # []
    # Test 3
    print(solution.letterCombinations("2"))  # ["a", "b", "c"]
    # Test supplémentaire
    print(solution.letterCombinations(
        "79"))  # ["pw", "px", "py", "pz", "qw", "qx", "qy", "qz", "rw", "rx", "ry", "rz", "sw", "sx", "sy", "sz"]
