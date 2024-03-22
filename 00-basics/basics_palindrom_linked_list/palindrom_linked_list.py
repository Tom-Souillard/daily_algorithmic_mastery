class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Checks if a singly linked list is a palindrome.

        Args:
        head: Optional[ListNode] - The head of the singly linked list.

        Returns:
        bool - True if the list is a palindrome, False otherwise.

        This method employs a fast and slow pointer technique to find the list's midpoint,
        reverses the second half, and then compares it with the first half. This ensures O(n) time
        complexity and O(1) space complexity.
        """

        lent = head
        rapide = head
        # Find the midpoint with slow and fast pointers
        while rapide and rapide.next:
            lent = lent.next
            rapide = rapide.next.next

        # Reverse the second half
        prev = None
        while lent:
            suivant = lent.next
            lent.next = prev
            prev = lent
            lent = suivant

        # Compare the first and second half
        gauche = head
        droite = prev
        while droite:
            if gauche.val != droite.val:
                return False
            gauche = gauche.next
            droite = droite.next

        return True
