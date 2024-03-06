class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Determines if a linked list has a cycle within it.

        This method uses the Floyd's Tortoise and Hare algorithm, where two pointers
        move at different speeds. If there is a cycle, the fast pointer (hare) will eventually
        meet the slow pointer (tortoise).

        Args:
        head: Optional[ListNode] - The head of the linked list.

        Returns:
        bool - True if there is a cycle in the linked list, otherwise False.
        """
        tortue = lievre = head
        while lievre and lievre.next:
            tortue = tortue.next
            lievre = lievre.next.next
            if tortue == lievre:
                return True
        return False
