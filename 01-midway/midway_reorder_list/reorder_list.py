class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Reorders the given singly linked list as per the specified format: L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ….
        This is done in-place, without modifying the values within the list's nodes.

        Args:
        head: Optional[ListNode] - The head of the singly linked-list to be reordered.

        Returns:
        None: Modifies the list in-place.
        """
        if not head or not head.next:
            return

        # Trouver le milieu
        rapide, lent = head, head
        while rapide and rapide.next:
            rapide = rapide.next.next
            lent = lent.next

        # Inverser la seconde moitié
        precedent, actuel = None, lent
        while actuel:
            suivant_temp = actuel.next
            actuel.next = precedent
            precedent = actuel
            actuel = suivant_temp

        # Fusionner les deux moitiés
        premiere, deuxieme = head, precedent
        while deuxieme.next:
            temp1, temp2 = premiere.next, deuxieme.next
            premiere.next = deuxieme
            deuxieme.next = temp1
            premiere, deuxieme = temp1, temp2
