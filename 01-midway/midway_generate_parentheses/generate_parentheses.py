from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Generates all combinations of well-formed parentheses.

        Args:
            n: An integer representing the number of pairs of parentheses.

        Returns:
            A list of strings, where each string represents a combination of well-formed parentheses.
        """
        def generer(combine, ouvert, ferme):
            if len(combine) == 2 * n:
                resultats.append(combine)
                return
            if ouvert < n:
                generer(combine + "(", ouvert + 1, ferme)
            if ferme < ouvert:
                generer(combine + ")", ouvert, ferme + 1)

        resultats = []
        generer("", 0, 0)
        return resultats

# Partie test
if __name__ == "__main__":
    solution = Solution()
    print(solution.generateParenthesis(3)) # Attendu : ["((()))","(()())","(())()","()(())","()()()"]
    print(solution.generateParenthesis(1)) # Attendu : ["()"]
    print(solution.generateParenthesis(2)) # Test supplémentaire : Attendu : ["(())", "()()"]
