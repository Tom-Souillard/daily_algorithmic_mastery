class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """
        Calculate the sum of the minimums of every subarray in the given array.

        Args:
        arr (List[int]): A list of integers.

        Returns:
        int: The sum of the minimums of every subarray modulo 10^9 + 7.
        """
        MOD = 10 ** 9 + 7
        n = len(arr)
        gauche = [0] * n
        droite = [0] * n

        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            gauche[i] = stack[-1] if stack else -1
            stack.append(i)

        stack.clear()
        for i in reversed(range(n)):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            droite[i] = stack[-1] if stack else n
            stack.append(i)

        resultat = sum((i - gauche[i]) * (droite[i] - i) * arr[i] for i in range(n)) % MOD
        return resultat
