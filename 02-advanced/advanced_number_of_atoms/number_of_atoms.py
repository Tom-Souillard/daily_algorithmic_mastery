from collections import defaultdict
import re


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        """
        Returns the count of each atom in a chemical formula.

        Args:
            formula (str): The chemical formula.

        Returns:
            str: The counts of each atom sorted by atom name.
        """

        def parse(formule: str, multiplicateur: int, index: int):
            n = len(formule)
            compteur = defaultdict(int)
            while index < n:
                if formule[index] == '(':
                    index += 1
                    sous_compteur, index = parse(formule, multiplicateur, index)
                    multiplicateur_actuel = 1
                    multiplicateur_match = re.match(r'\d+', formule[index:])
                    if multiplicateur_match:
                        multiplicateur_actuel = int(multiplicateur_match.group())
                        index += len(multiplicateur_match.group())
                    for elem, cnt in sous_compteur.items():
                        compteur[elem] += cnt * multiplicateur_actuel
                elif formule[index] == ')':
                    index += 1
                    break
                else:
                    elem_match = re.match(r'([A-Z][a-z]*)(\d*)', formule[index:])
                    element = elem_match.group(1)
                    nombre = int(elem_match.group(2)) if elem_match.group(2) else 1
                    compteur[element] += nombre * multiplicateur
                    index += len(elem_match.group(0))
            return compteur, index

        total_compteur, _ = parse(formula, 1, 0)
        resultat = ''.join(f"{elem}{(total_compteur[elem] if total_compteur[elem] > 1 else '')}"
                           for elem in sorted(total_compteur))
        return resultat


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.countOfAtoms("H2O") == "H2O"
    assert solution.countOfAtoms("Mg(OH)2") == "H2MgO2"
    assert solution.countOfAtoms("K4(ON(SO3)2)2") == "K4N2O14S4"
    print("All tests passed.")
