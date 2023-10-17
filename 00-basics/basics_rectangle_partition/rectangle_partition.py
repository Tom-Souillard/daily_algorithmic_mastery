from collections import Counter

def read_input():
    """Lire les entrées utilisateur."""
    width, height, _, _ = map(int, input().split())
    x_separators = [0] + [int(i) for i in input().split()] + [width]
    y_separators = [0] + [int(i) for i in input().split()] + [height]
    return x_separators, y_separators

def calculate_combinations(separators):
    """
    Calculer toutes les combinaisons possibles de distances
    entre les séparateurs.
    """
    return [separators[j] - separators[i] for i in range(len(separators)) for j in range(i + 1, len(separators))]

def count_squares(x_separators, y_separators):
    """Compter le nombre de carrés formés par les combinaisons de séparateurs."""
    x_combinations = Counter(calculate_combinations(x_separators))
    y_combinations = Counter(calculate_combinations(y_separators))

    return sum(freq * y_combinations[length] for length, freq in x_combinations.items())


if __name__ == "__main__":
    x_separators, y_separators = read_input()
    print(count_squares(x_separators, y_separators))