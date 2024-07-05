from typing import Optional, List


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        """
        Given the head of a linked list, returns an array containing the minimum and maximum distances between any two distinct critical points in the list.
        If there are fewer than two critical points, returns [-1, -1].

        Args:
            head (Optional[ListNode]): The head node of the linked list.

        Returns:
            List[int]: A list with two integers representing the minimum and maximum distances.
        """
        indices = []
        index = 1
        prev, current = head, head.next

        while current and current.next:
            next_node = current.next
            if (current.val > prev.val and current.val > next_node.val) or (
                    current.val < prev.val and current.val < next_node.val):
                indices.append(index)
            prev = current
            current = next_node
            index += 1

        if len(indices) < 2:
            return [-1, -1]

        min_distance = min(indices[i] - indices[i - 1] for i in range(1, len(indices)))
        max_distance = indices[-1] - indices[0]

        return [min_distance, max_distance]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    head1 = ListNode(3, ListNode(1))
    assert solution.nodesBetweenCriticalPoints(head1) == [-1, -1]

    head2 = ListNode(5, ListNode(3, ListNode(1, ListNode(2, ListNode(5, ListNode(1, ListNode(2)))))))
    assert solution.nodesBetweenCriticalPoints(head2) == [1, 3]

    head3 = ListNode(1, ListNode(3, ListNode(2, ListNode(2, ListNode(3, ListNode(2, ListNode(2, ListNode(2, ListNode(
        7)))))))))
    assert solution.nodesBetweenCriticalPoints(head3) == [3, 3]

    print("All tests passed.")
