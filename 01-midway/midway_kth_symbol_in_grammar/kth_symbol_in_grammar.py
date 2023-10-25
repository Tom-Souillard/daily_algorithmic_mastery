class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        """
        Returns the k-th (1-indexed) symbol in the n-th row of a table of n rows.
        The table is built by replacing each occurrence of 0 with 01 and each occurrence of 1 with 10.

        Args:
        n (int): The row number (1-indexed).
        k (int): The symbol number in the n-th row (1-indexed).

        Returns:
        int: The k-th symbol in the n-th row.
        """
        if n == 1:
            return 0
        k_precedent = (k - 1) // 2 + 1
        val_precedente = self.kthGrammar(n - 1, k_precedent)
        if k % 2 == 0:
            return 1 - val_precedente
        else:
            return val_precedente
