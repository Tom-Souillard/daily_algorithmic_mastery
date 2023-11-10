from collections import defaultdict

class Solution:
    def restoreArray(self, adjacentPairs):
        """
        Restore an array from its adjacent pairs.

        This function takes a list of adjacent pairs and reconstructs the original array.
        It uses a map to link each number to its adjacent pairs and then reconstructs
        the array by iteratively adding the next adjacent element.

        Args:
            adjacentPairs (List[List[int]]): A list of pairs representing adjacent elements.

        Returns:
            List[int]: The reconstructed array from the given adjacent pairs.
        """
        adj_map = defaultdict(list)
        for a, b in adjacentPairs:
            adj_map[a].append(b)
            adj_map[b].append(a)

        for key, value in adj_map.items():
            if len(value) == 1:
                start = key
                break

        result = [start]
        while len(result) < len(adjacentPairs) + 1:
            current = result[-1]
            next_elements = adj_map[current]
            for next_elem in next_elements:
                if len(result) == 1 or next_elem != result[-2]:
                    result.append(next_elem)
                    break

        return result
