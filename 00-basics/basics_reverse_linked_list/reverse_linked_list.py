class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses a singly linked list.

        This method iterates through the list once, using three pointers to reverse the list in place,
        achieving O(n) time complexity and O(1) space complexity.

        Args:
            head: The head node of the singly linked list.

        Returns:
            The new head node of the reversed singly linked list.
        """
        precedent = None
        courant = head
        while courant:
            suivant = courant.next
            courant.next = precedent
            precedent = courant
            courant = suivant
        return precedent
