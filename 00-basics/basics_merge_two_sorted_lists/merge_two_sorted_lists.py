from typing import Optional

# Définition de la classe ListNode pour créer des listes chaînées
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return dummy.next

# Fonction pour créer une liste chaînée à partir d'une liste Python
def list_to_linkedlist(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Fonction pour convertir une liste chaînée en liste Python pour affichage
def linkedlist_to_list(head):
    lst = []
    current = head
    while current:
        lst.append(current.val)
        current = current.next
    return lst

if __name__ == "__main__":
    sol = Solution()

    # Test 1
    list1 = list_to_linkedlist([1, 2, 4])
    list2 = list_to_linkedlist([1, 3, 4])
    merged = sol.mergeTwoLists(list1, list2)
    print("Exemple 1:", linkedlist_to_list(merged) == [1, 1, 2, 3, 4, 4])

    # Test 2
    list1 = list_to_linkedlist([])
    list2 = list_to_linkedlist([])
    merged = sol.mergeTwoLists(list1, list2)
    print("Exemple 2:", linkedlist_to_list(merged) == [])

    # Test 3
    list1 = list_to_linkedlist([])
    list2 = list_to_linkedlist([0])
    merged = sol.mergeTwoLists(list1, list2)
    print("Exemple 3:", linkedlist_to_list(merged) == [0])
