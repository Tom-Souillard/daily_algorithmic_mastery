class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Add two numbers represented by two linked lists.

        Each node contains a single digit, and the digits are stored in reverse order.
        The function returns the sum as a new linked list.

        Args:
        l1 (Optional[ListNode]): The head of the first linked list.
        l2 (Optional[ListNode]): The head of the second linked list.

        Returns:
        Optional[ListNode]: The head of the linked list representing the sum.
        """
        sommetete = ListNode(0)  # The head node of the result list
        courant = sommetete  # Current node in the result list
        retenue = 0  # Carry value for sum greater than 9

        while l1 or l2 or retenue:
            somme = retenue  # Start with carry value

            if l1:
                somme += l1.val  # Add value from l1
                l1 = l1.next  # Move to next node in l1

            if l2:
                somme += l2.val  # Add value from l2
                l2 = l2.next  # Move to next node in l2

            retenue = somme // 10  # Compute new carry
            courant.next = ListNode(somme % 10)  # Create new node with sum's unit place
            courant = courant.next  # Move to next node in result list

        return sommetete.next  # Return head of result list (skipping dummy head)
