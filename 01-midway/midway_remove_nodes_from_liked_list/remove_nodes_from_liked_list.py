from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse traverses the linked list and keeps only the nodes that have maximum values seen so far,
        then reverses again to restore original order with only the required nodes.

        Args:
        head (Optional[ListNode]): The head of the linked list.

        Returns:
        Optional[ListNode]: The head of the modified linked list.
        """
        if not head:
            return None
        # Reverse the linked list
        noeud_courant = head
        noeud_precedent = None
        while noeud_courant:
            noeud_suivant = noeud_courant.next
            noeud_courant.next = noeud_precedent
            noeud_precedent = noeud_courant
            noeud_courant = noeud_suivant

        # Filter the nodes
        max_valeur = float('-inf')
        noeud_courant = noeud_precedent
        noeud_precedent = None
        tete_filtrée = None
        while noeud_courant:
            if noeud_courant.val >= max_valeur:
                if tete_filtrée is None:
                    tete_filtrée = noeud_courant
                if noeud_precedent:
                    noeud_precedent.next = noeud_courant
                max_valeur = noeud_courant.val
                noeud_precedent = noeud_courant
            noeud_courant = noeud_courant.next

        if noeud_precedent:
            noeud_precedent.next = None

        # Reverse the filtered list to restore original order
        noeud_courant = tete_filtrée
        noeud_precedent = None
        while noeud_courant:
            noeud_suivant = noeud_courant.next
            noeud_courant.next = noeud_precedent
            noeud_precedent = noeud_courant
            noeud_courant = noeud_suivant
        return noeud_precedent


# Test cases
def test():
    l5 = ListNode(8)
    l4 = ListNode(3, l5)
    l3 = ListNode(13, l4)
    l2 = ListNode(2, l3)
    l1 = ListNode(5, l2)
    result = Solution().removeNodes(l1)
    while result:
        print(result.val, end=' -> ')
        result = result.next
    print("None")


test()
