from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Doubles the value represented by a singly-linked list of integers without converting the full number to an integer,
        avoiding overflow errors for very large numbers.

        Args:
        head (Optional[ListNode]): The head of the singly-linked list.

        Returns:
        Optional[ListNode]: The head of the new linked list representing double the original number.
        """
        chaine, courant = '', head
        while courant:
            chaine += str(courant.val)
            courant = courant.next

        retenue = 0
        result = []
        for chiffre in reversed(chaine):
            temp = int(chiffre) * 2 + retenue
            retenue = temp // 10
            result.append(temp % 10)

        if retenue:
            result.append(retenue)

        result.reverse()
        nouveau_tete = ListNode(result[0])
        courant = nouveau_tete
        for chiffre in result[1:]:
            courant.next = ListNode(chiffre)
            courant = courant.next

        return nouveau_tete


# Test cases
if __name__ == "__main__":
    l1 = ListNode(9)
    current = l1
    for _ in range(999):
        current.next = ListNode(9)
        current = current.next
    solution = Solution()
    resultat = solution.doubleIt(l1)
    while resultat:
        print(resultat.val, end='')
        resultat = resultat.next
        if resultat:
            print(" -> ", end='')
    print()
