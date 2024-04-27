class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        """
        Given a `ring` and a `key`, determines the minimum number of steps required
        to spell out the `key` using the `ring`, where each character of the key
        needs to be aligned at the "12:00" direction by rotating the ring clockwise
        or anticlockwise and then pressing a button to spell the character.

        Args:
        ring (str): The string representing the ring configuration.
        key (str): The string representing the keyword to spell.

        Returns:
        int: The minimum number of steps required to spell the key.

        """
        from collections import defaultdict, deque

        def minDistance(start, end):
            return min(abs(start - end), len(ring) - abs(start - end))

        position = defaultdict(list)
        for i, char in enumerate(ring):
            position[char].append(i)

        dp = {}
        queue = deque([(0, 0)])
        for i in range(len(key)):
            next_queue = deque()
            while queue:
                cur_char_idx, ring_idx = queue.popleft()
                for next_ring_idx in position[key[i]]:
                    next_step = minDistance(ring_idx, next_ring_idx) + 1
                    if (i, next_ring_idx) in dp:
                        dp[(i, next_ring_idx)] = min(dp[(i, next_ring_idx)], dp[(cur_char_idx, ring_idx)] + next_step)
                    else:
                        dp[(i, next_ring_idx)] = dp.get((cur_char_idx, ring_idx), 0) + next_step
                        next_queue.append((i, next_ring_idx))
            queue = next_queue

        return min(dp[(len(key) - 1, idx)] for idx in position[key[-1]])

# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.findRotateSteps("godding", "gd"))  # Expected output: 4
    print(sol.findRotateSteps("godding", "godding"))  # Expected output: 13
    print(sol.findRotateSteps("ababcab", "acba"))  # Expected output: 9
