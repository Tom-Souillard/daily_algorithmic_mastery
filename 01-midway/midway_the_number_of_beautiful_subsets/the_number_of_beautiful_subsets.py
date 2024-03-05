from collections import Counter

class Solution:
    def beautifulSubsets(self, nums: list[int], k: int) -> int:
        """
        Returns the number of non-empty beautiful subsets of the array nums.

        Args:
            nums (List[int]): An array of positive integers.
            k (int): A positive integer.

        Returns:
            int: The number of beautiful subsets.
        """
        def count_beautiful_subsets(freq, num_counts):
            if not num_counts:
                return 1
            current = num_counts.pop()
            without_current = count_beautiful_subsets(freq, num_counts.copy())
            with_current = 0
            if current - k not in freq or freq[current - k] == 0:
                if current + k not in freq or freq[current + k] == 0:
                    freq[current] += 1
                    with_current = count_beautiful_subsets(freq, num_counts.copy())
                    freq[current] -= 1
            return without_current + with_current

        num_counts = list(Counter(nums).elements())
        return count_beautiful_subsets(Counter(), num_counts) - 1

# Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.beautifulSubsets([2, 4, 6], 2))  # Output: 4
    print(s.beautifulSubsets([1], 1))        # Output: 1
    print(s.beautifulSubsets([1, 3, 5], 2))  # Output: 7
    print(s.beautifulSubsets([1, 2, 3, 4], 1))  # Output: 11
