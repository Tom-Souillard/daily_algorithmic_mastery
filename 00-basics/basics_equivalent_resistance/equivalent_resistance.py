import sys
import re
from typing import Dict, List, Union, Optional


def read_key_value_pairs(n: int, value_type: type = float) -> Dict[str, Union[int, float]]:
    """
    Lit n paires clé-valeur depuis l'entrée standard.

    Args:
        n (int): Nombre de paires à lire.
        value_type (type, optional): Type des valeurs. Par défaut à float.

    Returns:
        Dict[str, Union[int, float]]: Dictionnaire des paires clé-valeur.
    """
    pairs = {}
    for _ in range(n):
        key, value = input().split()
        pairs[key] = value_type(value)
    return pairs


def replace_key_with_value(input_str: str, replacement_dictionary: Dict[str, Union[int, float]]) -> str:
    """
    Remplace chaque instance des clés présentes dans la chaîne de caractères par la valeur correspondante dans le dictionnaire.
    Args:
        input_str (str): Chaîne d'entrée.
        replacement_dictionary (Dict[str, Union[int, float]]): Dictionnaire de remplacement.

    Returns:
        str: Chaîne modifiée.
    """
    pattern = re.compile('|'.join(map(re.escape, replacement_dictionary.keys())))
    return pattern.sub(lambda match: str(replacement_dictionary[match.group(0)]), input_str)


def replace_str_by_float(input_str: str, pattern_str: str = r"[\(\)\[\]]|\d+\.\d+|\d+") -> List[Union[str, float]]:
    """
    Convertit les éléments numériques d'une chaîne en floats.

    Args:
        input_str (str): Chaîne d'entrée.
        pattern_str (str, optional): Expression régulière pour le filtrage. Par défaut à r"[\(\)\[\]]|\d+\.\d+|\d+".
            \(       |  # parenthèse ouvrante
            \)       |  # parenthèse fermante
            \[       |  # crochet ouvrant
            \]       |  # crochet fermant
            \d+\.\d+ |  # nombre à virgule flottante
            \d+        # nombre entier

    Returns:
        List[Union[str, float]]: Liste des éléments.
    """
    pattern = re.compile(pattern_str)
    elements = pattern.findall(input_str)
    return [float(x) if x.replace('.', '', 1).isdigit() else x for x in elements]


def sum_values(values: List[Union[int, float]]) -> float:
    """
    Calcule la somme des valeurs dans une liste.

    Args:
        values (List[Union[int, float]]): Liste des valeurs.

    Returns:
        float: Somme des valeurs.
    """
    return sum(values)


def inverse_sum_of_inverses(values: List[Union[int, float]]) -> float:
    """
    Calcule l'inverse de la somme des inverses des valeurs dans une liste.

    Args:
        values (List[Union[int, float]]): Liste des valeurs.

    Returns:
        float: Inverse de la somme des inverses.
    """
    return 1 / sum(1 / val for val in values)


def format_number(number: float, precision: int = 1) -> float:
    """
    Formate un nombre à une précision donnée.

    Args:
        number (float): Nombre à formater.
        precision (int, optional): Nombre de chiffres après la virgule. Par défaut à 1.

    Returns:
        float: Nombre formaté.
    """
    return round(number, precision)


def evaluate_expression(expression: List[Union[str, float]]) -> float:
    """
    Évalue une expression de circuit électrique.

    Args:
        expression (List[Union[str, float]]): Expression sous forme de liste.

    Returns:
        float: Résistance équivalente.
    """
    stack = []
    for item in expression:
        if item not in [')', ']']:
            stack.append(item)
        else:
            temp = []
            while stack[-1] not in ['(', '[']:
                temp.append(stack.pop())
            stack.pop()
            temp.reverse()

            if item == ')':
                stack.append(sum_values(temp))
            elif item == ']':
                stack.append(inverse_sum_of_inverses(temp))
    return stack[0]


if __name__ == "__main__":
    try:
        n = int(input())
        if n <= 0 or n >= 10:
            raise ValueError("Le nombre de paires clé-valeur doit être entre 1 et 9.")

        resistor_dic = read_key_value_pairs(n)
        for key, value in resistor_dic.items():
            if value <= 0 or value >= 100:
                raise ValueError("La résistance doit être entre 1 et 99.")

        circuit_str = input()
        if not circuit_str:
            raise ValueError("La chaîne de circuit ne peut pas être vide.")

        new_circuit = replace_key_with_value(circuit_str, resistor_dic)
        final_circuit = replace_str_by_float(new_circuit)
        result = evaluate_expression(final_circuit)
        print(format_number(result))

    except ValueError as error_message:
        print(f"Erreur: {error_message}")