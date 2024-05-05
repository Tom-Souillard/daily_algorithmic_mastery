# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, noeud):
        """
        Deletes the node from the linked list that is given as input.

        This function will modify the linked list by replacing the value of the given node
        with the value of the next node and then by skipping the next node.

        Args:
            noeud (ListNode): The node that needs to be deleted from the linked list.

        Returns:
            None: Modifies the linked list in place, does not return anything.
        """
        noeud.val = noeud.next.val
        noeud.next = noeud.next.next


# Test cases
if __name__ == "__main__":
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None


    def printList(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        print("->".join(map(str, result)))


    def createLinkedList(values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for value in values[1:]:
            current.next = ListNode(value)
            current = current.next
        return head


    # Test case 1
    liste1 = createLinkedList([4, 5, 1, 9])
    node_to_delete = liste1.next  # Node with value 5
    Solution().deleteNode(node_to_delete)
    printList(liste1)  # Expected Output: 4->1->9

    # Test case 2
    liste2 = createLinkedList([4, 5, 1, 9])
    node_to_delete = liste2.next.next  # Node with value 1
    Solution().deleteNode(node_to_delete)
    printList(liste2)  # Expected Output: 4->5->9
