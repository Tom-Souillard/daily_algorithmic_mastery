class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        """
        Determines if it is possible to provide the correct change for each customer
        based on the bills they pay with.

        Args:
            bills (list[int]): A list of integers representing the bills each customer pays with.

        Returns:
            bool: True if every customer can be provided with the correct change, False otherwise.
        """
        cinq, dix = 0, 0
        for billet in bills:
            if billet == 5:
                cinq += 1
            elif billet == 10:
                if cinq == 0:
                    return False
                cinq -= 1
                dix += 1
            else:
                if dix > 0 and cinq > 0:
                    dix -= 1
                    cinq -= 1
                elif cinq >= 3:
                    cinq -= 3
                else:
                    return False
        return True

# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.lemonadeChange([5,5,5,10,20]) == True
    assert solution.lemonadeChange([5,5,10,10,20]) == False
    assert solution.lemonadeChange([5,5,5,5,10,5,10,10,20]) == True
    assert solution.lemonadeChange([10,10]) == False
    print("All tests passed.")
