class Solution:
    def pivotInteger(self, n: int) -> int:
        """
        Finds the pivot integer 'x' for a given positive integer 'n' where the sum
        of all integers from 1 to 'x' equals the sum of all integers from 'x' to 'n'.
        If no such 'x' exists, returns -1.

        Args:
        n: An integer representing the upper bound of the range to search for a pivot.

        Returns:
        An integer representing the pivot 'x' if it exists, otherwise -1.
        """
        sommeTotale = sum([i for i in range(n+1)])
        sommeInverse, pivot = n, n

        while pivot:
            if sommeTotale == sommeInverse:
                return pivot
            sommeTotale -= pivot
            sommeInverse += pivot - 1
            pivot -= 1

        return -1
