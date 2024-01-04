from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Swaps every two adjacent nodes in a linked list.

        Args:
        head (Optional[ListNode]): The head of the linked list.

        Returns:
        Optional[ListNode]: The head of the modified linked list.
        """
        prelude = ListNode(0)
        prelude.next = head
        actuel = prelude
        while actuel.next and actuel.next.next:
            a = actuel.next
            b = actuel.next.next
            actuel.next, a.next, b.next = b, b.next, a
            actuel = a
        return prelude.next


# Partie test
if __name__ == "__main__":
    # Aide pour construire la liste
    def construire_liste(elements):
        head = actuel = ListNode(0)
        for element in elements:
            actuel.next = ListNode(element)
            actuel = actuel.next
        return head.next


    def imprimer_liste(head):
        elements = []
        while head:
            elements.append(head.val)
            head = head.next
        return elements


    solution = Solution()

    # Test 1
    liste1 = construire_liste([1, 2, 3, 4])
    print(imprimer_liste(solution.swapPairs(liste1)))  # Devrait afficher [2, 1, 4, 3]

    # Test 2
    liste2 = construire_liste([])
    print(imprimer_liste(solution.swapPairs(liste2)))  # Devrait afficher []

    # Test 3
    liste3 = construire_liste([1])
    print(imprimer_liste(solution.swapPairs(liste3)))  # Devrait afficher [1]

    # Test 4
    liste4 = construire_liste([1, 2, 3, 4, 5])
    print(imprimer_liste(solution.swapPairs(liste4)))  # Devrait afficher [2, 1, 4, 3, 5]
