class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Finds and returns the middle node of a singly linked list. If the list has an even number of nodes,
        it returns the second middle node.

        Args:
        head: Optional[ListNode] - The head of the singly linked list.

        Returns:
        Optional[ListNode] - The middle node of the list.
        """
        rapide = lent = head
        while rapide and rapide.next:
            lent = lent.next
            rapide = rapide.next.next
        return lent
