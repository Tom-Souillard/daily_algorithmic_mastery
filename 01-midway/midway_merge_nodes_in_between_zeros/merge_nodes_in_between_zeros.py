from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merges nodes in a linked list between zeros into a single node with the sum of the merged nodes' values.

        Args:
            head (Optional[ListNode]): The head of the linked list.

        Returns:
            Optional[ListNode]: The head of the modified linked list without zeros.
        """
        actuel = head.next
        resultat = ListNode()
        queue = resultat
        somme = 0

        while actuel:
            if actuel.val == 0:
                if somme != 0:
                    queue.next = ListNode(somme)
                    queue = queue.next
                    somme = 0
            else:
                somme += actuel.val
            actuel = actuel.next

        return resultat.next


# Test cases
if __name__ == "__main__":
    solution = Solution()


    def creer_liste(vals):
        tete = ListNode(0)
        courant = tete
        for val in vals:
            courant.next = ListNode(val)
            courant = courant.next
        return tete


    def extraire_vals(tete):
        vals = []
        courant = tete
        while courant:
            vals.append(courant.val)
            courant = courant.next
        return vals


    assert extraire_vals(solution.mergeNodes(creer_liste([0, 3, 1, 0, 4, 5, 2, 0]))) == [4, 11]
    assert extraire_vals(solution.mergeNodes(creer_liste([0, 1, 0, 3, 0, 2, 2, 0]))) == [1, 3, 4]
    assert extraire_vals(solution.mergeNodes(creer_liste([0, 0, 0]))) == []
    assert extraire_vals(solution.mergeNodes(creer_liste([0, 1, 2, 3, 0, 4, 5, 0, 0, 6, 7, 8, 0]))) == [6, 9, 21]

    print("All tests passed.")