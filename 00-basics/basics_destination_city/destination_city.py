def destCity(paths):
    """
    Finds the destination city in a list of direct paths.

    Args:
    paths (List[List[str]]): A list of direct paths between cities.

    Returns:
    str: The destination city.

    The function uses a set to store the starting cities and then iterates
    through the paths. If a city is not in the starting cities set, it is the destination.
    """
    villesDepart = set()
    for depart, arrivee in paths:
        villesDepart.add(depart)

    for depart, arrivee in paths:
        if arrivee not in villesDepart:
            return arrivee

# Example usage
paths1 = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
example1 = destCity(paths1)  # Output: "Sao Paulo"

paths2 = [["B","C"],["D","B"],["C","A"]]
example2 = destCity(paths2)  # Output: "A"

paths3 = [["A","Z"]]
example3 = destCity(paths3)  # Output: "Z"
