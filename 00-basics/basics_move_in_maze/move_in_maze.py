from typing import TypeVar, Callable, Dict, List, Tuple, Optional
from collections import deque

T = TypeVar('T')  # Type de Noeud


class Maze:
    def __init__(self, data: List[List[str]], start_symbol: str = 'S', open_symbol: str = '.', wall_symbol: str = '#'):
        """
        Initialise un labyrinthe avec des données fournies.

        Args:
            data (List[List[str]]): Une liste de listes de chaînes représentant le labyrinthe.
            start_symbol (str): Le symbole représentant le point de départ dans le labyrinthe.
            open_symbol (str): Le symbole représentant un espace ouvert dans le labyrinthe.
            wall_symbol (str): Le symbole représentant un mur dans le labyrinthe.

        Raises:
            ValueError: Si les dimensions du labyrinthe ne respectent pas les contraintes.
        """
        if not (3 <= len(data) <= 30) or not all(3 <= len(row) <= 30 for row in data):
            raise ValueError("Les dimensions du labyrinthe doivent être comprises entre 3 et 30.")

        self.data = data
        self.start_symbol = start_symbol
        self.open_symbol = open_symbol
        self.wall_symbol = wall_symbol
        self.rows, self.columns = len(data), len(data[0])
        self.start_coordinates = self.find_start_coordinates()

    def find_start_coordinates(self) -> Optional[Tuple[int, int]]:
        """
        Trouve les coordonnées du point de départ dans le labyrinthe.

        Returns:
            Tuple[int, int] | None: Un tuple représentant les coordonnées de départ, ou None si non trouvé.
        """
        for i, row in enumerate(self.data):
            for j, cell in enumerate(row):
                if cell == self.start_symbol:
                    return i, j

    def get_neighbors(self, coord: Tuple[int, int]) -> List[Tuple[int, int]]:
        """
        Obtient les voisins d'une cellule donnée.

        Args:
            coord (Tuple[int, int]): Les coordonnées de la cellule.

        Returns:
            List[Tuple[int, int]]: Une liste de coordonnées voisines.
        """
        x, y = coord
        neighbors = []
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = (x + dx) % self.rows, (y + dy) % self.columns
            if self.data[nx][ny] != self.wall_symbol:
                neighbors.append((nx, ny))
        return neighbors


def generic_bfs(start: T, get_neighbors: Callable[[T], List[T]]) -> Dict[T, int]:
    """
    Effectue une recherche en largeur dans un graphe générique à partir d'un point de départ.

    Args:
        start (T): Le point de départ de la recherche.
        get_neighbors (Callable[[T], List[T]]): Une fonction pour obtenir les voisins d'un noeud.

    Returns:
        Dict[T, int]: Un dictionnaire représentant la distance de chaque nœud accessible depuis le départ.
    """
    distances = {start: 0}
    queue = deque([start])
    while queue:
        current_node = queue.popleft()
        for neighbor in get_neighbors(current_node):
            if neighbor not in distances:
                distances[neighbor] = distances[current_node] + 1
                if distances[neighbor] > 35:
                    raise ValueError("Il y a plus de 35 mouvements nécessaires pour atteindre un point.")
                queue.append(neighbor)
    return distances


def display_maze_with_distances(maze: Maze, distances: Dict[Tuple[int, int], int]) -> None:
    """
    Affiche un labyrinthe avec les distances depuis le point de départ.

    Args:
        maze (Maze): Un objet Maze représentant le labyrinthe.
        distances (Dict[Tuple[int, int], int]): Un dictionnaire représentant les distances depuis le point de départ.
    """
    data = [row[:] for row in maze.data]  # copie profonde des données du labyrinthe
    for coord, distance in distances.items():
        x, y = coord
        # Convertir les distances en caractères, 0-9 puis A-Z
        if distance <= 9:
            data[x][y] = str(distance)
        elif distance <= 35:
            data[x][y] = chr(ord('A') + distance - 10)
        else:
            data[x][y] = maze.open_symbol  # ou autre caractère pour indiquer l'inaccessibilité
    for row in data:
        print(''.join(row))


if __name__ == "__main__":
    w, h = [int(i) for i in input().split()]
    lst_maze = [input() for _ in range(h)]
    maze_data = [list(x) for x in lst_maze]
    maze = Maze(maze_data)
    if maze.start_coordinates:
        distances = generic_bfs(maze.start_coordinates, maze.get_neighbors)
        display_maze_with_distances(maze, distances)
    else:
        print("Point de départ 'S' non trouvé dans le labyrinthe.")
