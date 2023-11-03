class Solution:
    def buildArray(self, cible: List[int], n: int) -> List[str]:
        """ Generate a list of stack operations to form a target stack from a stream of integers.

        Args:
            cible (List[int]): The target stack represented as a list of integers that we want to construct.
            n (int): The maximum integer that can be pushed onto the stack from the stream.

        Returns:
            List[str]: A list of strings representing the required stack operations ("Push" or "Pop") to construct the target stack.
         """
        operations = []
        indice_cible = 0

        for nombre in range(1, n + 1):
            if indice_cible < len(cible) and nombre == cible[indice_cible]:
                operations.append("Push")
                indice_cible += 1
            elif indice_cible < len(cible):
                operations.append("Push")
                operations.append("Pop")
            else:
                break

        return operations
