from typing import List


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        """
        Détermine la santé des robots restants après toutes les collisions.

        Args:
            positions: Une liste d'entiers représentant les positions initiales des robots.
            healths: Une liste d'entiers représentant les santés initiales des robots.
            directions: Une chaîne représentant les directions de mouvement des robots ('L' pour gauche, 'R' pour droite).

        Returns:
            Une liste d'entiers représentant les santés des robots survivants dans leur ordre initial.
        """
        n = len(positions)
        pile = []
        robots = []

        for i in range(n):
            robots.append(
                {'position': positions[i], 'sante': healths[i], 'direction': directions[i], 'index_original': i})

        robots.sort(key=lambda x: x['position'])

        for i in range(n):
            if robots[i]['direction'] == 'L':
                while pile and robots[pile[-1]]['direction'] == 'R' and robots[pile[-1]]['sante'] < robots[i]['sante']:
                    pile.pop()
                    robots[i]['sante'] -= 1
                if not pile or robots[pile[-1]]['direction'] == 'L':
                    pile.append(i)
                elif pile and robots[pile[-1]]['sante'] == robots[i]['sante']:
                    pile.pop()
                elif pile and robots[pile[-1]]['sante'] > robots[i]['sante']:
                    robots[pile[-1]]['sante'] -= 1
            else:
                pile.append(i)

        return [robots[i]['sante'] for i in sorted(pile, key=lambda x: robots[x]['index_original'])]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.survivedRobotsHealths([5, 4, 3, 2, 1], [2, 17, 9, 15, 10], "RRRRR") == [2, 17, 9, 15, 10]
    assert solution.survivedRobotsHealths([3, 5, 2, 6], [10, 10, 15, 12], "RLRL") == [14]
    assert solution.survivedRobotsHealths([1, 2, 5, 6], [10, 10, 11, 11], "RLRL") == []
    print("All tests passed.")
