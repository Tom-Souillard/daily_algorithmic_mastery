class Solution:
    def isPathCrossing(self, path: str) -> bool:
        """
        Determine if the given path crosses itself.

        Args:
        path (str): A string consisting of 'N', 'S', 'E', 'W' indicating moves in
                    north, south, east, and west directions, respectively.

        Returns:
        bool: True if the path crosses itself at any point, False otherwise.
        """
        coordonnees_visitees = {(0, 0)}
        x, y = 0, 0

        for direction in path:
            if direction == 'N':
                y += 1
            elif direction == 'S':
                y -= 1
            elif direction == 'E':
                x += 1
            elif direction == 'W':
                x -= 1

            if (x, y) in coordonnees_visitees:
                return True
            coordonnees_visitees.add((x, y))

        return False
