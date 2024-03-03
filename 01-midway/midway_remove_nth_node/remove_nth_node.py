class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Remove the nth node from the end of the list and return its head.

        Given the head of a linked list and an integer n, this function removes
        the nth node from the end of the list and returns the new head of the list.

        Args:
            head: Optional[ListNode] - The head of the linked list.
            n: int - The position of the node to remove from the end of the list.

        Returns:
            Optional[ListNode] - The head of the modified list.

        Time Complexity: O(L), where L is the number of nodes in the list.
        Space Complexity: O(1), only uses constant extra space.
        """
        debut = ListNode(0)
        debut.next = head
        premier = retard = debut

        for _ in range(n + 1):
            premier = premier.next

        while premier:
            premier = premier.next
            retard = retard.next

        retard.next = retard.next.next

        return debut.next
