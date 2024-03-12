class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Remove all consecutive sequences of nodes that sum to 0 from a linked list.

        Args:
            head: The head of the linked list.

        Returns:
            The head of the modified list after removing zero sum sequences.
        """
        prefix = ListNode(0)
        prefix.next = head
        prefix_sum = 0
        somme_prefixes = {0: prefix}

        while head:
            prefix_sum += head.val
            if prefix_sum in somme_prefixes:
                prev = somme_prefixes[prefix_sum]
                somme = prefix_sum
                while prev.next != head:
                    prev = prev.next
                    somme += prev.val
                    if prev != head:
                        somme_prefixes.pop(somme)
                somme_prefixes[prefix_sum].next = head.next
            else:
                somme_prefixes[prefix_sum] = head
            head = head.next

        return prefix.next
