class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Evaluate the value of an arithmetic expression in Reverse Polish Notation.

        Args:
        tokens (List[str]): A list of strings representing the expression.

        Returns:
        int: The result of the expression.
        """
        pile = []
        for token in tokens:
            if token not in "+-*/":
                pile.append(int(token))
            else:
                droit = pile.pop()
                gauche = pile.pop()
                if token == '+':
                    pile.append(gauche + droit)
                elif token == '-':
                    pile.append(gauche - droit)
                elif token == '*':
                    pile.append(gauche * droit)
                elif token == '/':
                    pile.append(int(gauche / droit))  # Truncate towards zero
        return pile.pop()
