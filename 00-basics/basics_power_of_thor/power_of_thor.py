def get_direction(source_x: int, source_y: int, target_x: int, target_y: int, directions: dict) -> str:
    """
    Calcule la direction du point source vers la cible en utilisant un dictionnaire de directions.

    Args:
        source_x (int): Coordonnée X du point source.
        source_y (int): Coordonnée Y du point source.
        target_x (int): Coordonnée X de la cible.
        target_y (int): Coordonnée Y de la cible.
        directions (dict): Dictionnaire des directions possibles et de leurs abréviations.

    Returns:
        str: Direction du point source vers la cible (ex: "NE", "S", "W").
    """
    dir_y = directions['SAME']
    dir_x = directions['SAME']

    if source_y > target_y:
        dir_y = directions['UP']
    elif source_y < target_y:
        dir_y = directions['DOWN']

    if source_x > target_x:
        dir_x = directions['LEFT']
    elif source_x < target_x:
        dir_x = directions['RIGHT']

    return dir_y + dir_x


def move_in_direction(x: int, y: int, direction: str, mapping: dict, step: int = 1) -> (int, int):
    """
    Déplace un point dans une direction donnée.

    Args:
        x (int): Coordonnée X actuelle.
        y (int): Coordonnée Y actuelle.
        direction (str): Direction du mouvement.
        mapping (dict): Dictionnaire mappant les directions aux opérations.
        step (int, optional): Nombre de pas à faire dans la direction. Par défaut à 1.

    Returns:
        tuple: Nouvelles coordonnées (x, y) après le mouvement.
    """
    if mapping['UP'] in direction:
        y -= step
    if mapping['DOWN'] in direction:
        y += step
    if mapping['LEFT'] in direction:
        x -= step
    if mapping['RIGHT'] in direction:
        x += step

    return x, y

def is_within_bounds(x: int, y: int, width: int, height: int) -> bool:
    """
    Vérifie si un point est à l'intérieur des limites définies.

    Args:
        x (int): Coordonnée X du point.
        y (int): Coordonnée Y du point.
        width (int): Largeur de la zone.
        height (int): Hauteur de la zone.

    Returns:
        bool: True si le point est à l'intérieur des limites, sinon False.
    """
    return 0 <= x < width and 0 <= y < height

def main():
    DIRECTIONS = {
        'UP': 'S',
        'DOWN': 'N',
        'LEFT': 'E',
        'RIGHT': 'W',
        'SAME': ''
    }

    MAP_WIDTH = 40
    MAP_HEIGHT = 18

    x, y, target_x, target_y = [int(i) for i in input().split()]

    while True:
        _ = input()
        direction = get_direction(x, y, target_x, target_y, DIRECTIONS)
        new_x, new_y = move_in_direction(x, y, direction, DIRECTIONS)

        if not is_within_bounds(new_x, new_y, MAP_WIDTH, MAP_HEIGHT):
            break

        x, y = new_x, new_y
        print(direction)

if __name__ == "__main__":
    main()
