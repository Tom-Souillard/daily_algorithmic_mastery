class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        """
        Merges two singly-linked lists by replacing a segment from the first list with the second list.

        The nodes from the 'a'th to the 'b'th node in 'list1' are replaced by all nodes in 'list2'.
        
        Args:
            list1: The first singly-linked list.
            a: The starting index of the segment in 'list1' to be replaced.
            b: The ending index of the segment in 'list1' to be replaced.
            list2: The second singly-linked list to be inserted in 'list1'.

        Returns:
            The head of the modified 'list1', with the segment [a, b] replaced by 'list2'.
        """
        debut = list1  # Pointeur au début de la liste 'list1' avant la section à remplacer.
        for i in range(a - 1):
            debut = debut.next  # Avancer jusqu'au noeud juste avant 'a'.

        fin = debut.next  # Pointeur au début de la section à remplacer.
        for i in range(a, b + 1):
            fin = fin.next  # Avancer jusqu'au noeud juste après 'b'.

        debut.next = list2  # Connecter 'debut' au début de 'list2'.

        fin_list2 = list2
        while fin_list2.next:
            fin_list2 = fin_list2.next  # Avancer jusqu'au dernier noeud de 'list2'.

        fin_list2.next = fin  # Connecter la fin de 'list2' au reste de 'list1' après 'b'.

        return list1
