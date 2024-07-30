class Solution:
    def minimumDeletions(self, s: str) -> int:
        """
        Calculate the minimum number of deletions needed to make a string balanced.
        
        Args:
            s (str): The input string consisting only of characters 'a' and 'b'.
        
        Returns:
            int: The minimum number of deletions required.
        """
        nb_a = 0
        nb_b = 0
        for char in s:
            if char == 'a':
                nb_a += 1
            else:
                nb_b += 1
            nb_a = min(nb_a, nb_b)
        return nb_a

# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.minimumDeletions("aababbab") == 2
    assert solution.minimumDeletions("bbaaaaabb") == 2
    assert solution.minimumDeletions("ab") == 0
    assert solution.minimumDeletions("ba") == 1
    assert solution.minimumDeletions("aaa") == 0
    assert solution.minimumDeletions("bbb") == 0
    print("All tests passed.")
      
