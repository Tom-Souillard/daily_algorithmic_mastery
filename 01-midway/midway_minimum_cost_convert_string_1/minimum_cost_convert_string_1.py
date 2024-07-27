import heapq
from collections import defaultdict


class Solution:
    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        """
        Calculate the minimum cost to convert the string source to the string target using given character changes and their respective costs.

        Args:
            source (str): The initial string.
            target (str): The desired string.
            original (list[str]): The list of characters in the original string that can be changed.
            changed (list[str]): The list of characters to change to.
            cost (list[int]): The list of costs associated with each change.

        Returns:
            int: The minimum cost to convert source to target, or -1 if impossible.
        """
        if len(source) != len(target):
            return -1

        graph = defaultdict(list)
        for o, c, z in zip(original, changed, cost):
            graph[o].append((z, c))

        def dijkstra(start: str) -> dict:
            pq = [(0, start)]
            dist = {start: 0}
            while pq:
                current_cost, current_char = heapq.heappop(pq)
                if current_cost > dist.get(current_char, float('inf')):
                    continue
                for add_cost, neighbor in graph[current_char]:
                    new_cost = current_cost + add_cost
                    if new_cost < dist.get(neighbor, float('inf')):
                        dist[neighbor] = new_cost
                        heapq.heappush(pq, (new_cost, neighbor))
            return dist

        min_cost = {}
        all_chars = set(source + target + ''.join(original) + ''.join(changed))
        for char in all_chars:
            min_cost[char] = dijkstra(char)

        total_cost = 0
        for s_char, t_char in zip(source, target):
            if s_char == t_char:
                continue
            change_cost = min_cost[s_char].get(t_char, float('inf'))
            if change_cost == float('inf'):
                return -1
            total_cost += change_cost

        return total_cost


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.minimumCost("abcd", "acbe", ["a", "b", "c", "c", "e", "d"], ["b", "c", "b", "e", "b", "e"],
                                [2, 5, 5, 1, 2, 20]) == 28
    assert solution.minimumCost("aaaa", "bbbb", ["a", "c"], ["c", "b"], [1, 2]) == 12
    assert solution.minimumCost("abcd", "abce", ["a"], ["e"], [10000]) == -1
    print("All tests passed.")
