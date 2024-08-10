class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        """
        Returns a list of strings representing the FizzBuzz sequence up to n.

        Args:
            n (int): The upper limit of the FizzBuzz sequence.

        Returns:
            List[str]: The FizzBuzz sequence as a list of strings.
        """
        resultat = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                resultat.append("FizzBuzz")
            elif i % 3 == 0:
                resultat.append("Fizz")
            elif i % 5 == 0:
                resultat.append("Buzz")
            else:
                resultat.append(str(i))
        return resultat

# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.fizzBuzz(3) == ["1","2","Fizz"]
    assert solution.fizzBuzz(5) == ["1","2","Fizz","4","Buzz"]
    assert solution.fizzBuzz(15) == ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
    print("All tests passed.")