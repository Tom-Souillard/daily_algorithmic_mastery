from collections import deque, defaultdict
from typing import List, Dict, Deque


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        """
        Build a k x k matrix with numbers from 1 to k that satisfies the given row and column conditions.

        Args:
            k (int): The size of the matrix and the range of numbers to be placed in the matrix.
            rowConditions (List[List[int]]): List of conditions [above, below] indicating that 'above' should be in a row above 'below'.
            colConditions (List[List[int]]): List of conditions [left, right] indicating that 'left' should be in a column left of 'right'.

        Returns:
            List[List[int]]: A k x k matrix with numbers from 1 to k satisfying the given conditions, or an empty list if no valid matrix can be constructed.
        """

        def topological_sort(n: int, conditions: List[List[int]]) -> List[int]:
            """
            Perform topological sort on the given conditions.

            Args:
                n (int): The number of nodes in the graph (equal to k).
                conditions (List[List[int]]): List of conditions indicating directed edges in the graph.

            Returns:
                List[int]: A topologically sorted list of nodes, or an empty list if no valid ordering exists.
            """
            graph: Dict[int, List[int]] = defaultdict(list)
            in_degree: Dict[int, int] = {i: 0 for i in range(1, n + 1)}
            for u, v in conditions:
                graph[u].append(v)
                in_degree[v] += 1

            queue: Deque[int] = deque([node for node in in_degree if in_degree[node] == 0])
            order: List[int] = []
            while queue:
                node = queue.popleft()
                order.append(node)
                for neighbor in graph[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)

            return order if len(order) == n else []

        row_order = topological_sort(k, rowConditions)
        col_order = topological_sort(k, colConditions)

        if not row_order or not col_order:
            return []

        row_pos = {num: i for i, num in enumerate(row_order)}
        col_pos = {num: i for i, num in enumerate(col_order)}

        matrix = [[0] * k for _ in range(k)]
        for num in range(1, k + 1):
            matrix[row_pos[num]][col_pos[num]] = num

        return matrix

