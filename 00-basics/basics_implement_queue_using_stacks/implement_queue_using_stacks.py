class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pile_entree = []
        self.pile_sortie = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.

        Args:
        x (int): The element to push onto the queue.
        """
        self.pile_entree.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.

        Returns:
        int: The front element of the queue.
        """
        self.transfer_si_necessaire()
        return self.pile_sortie.pop()

    def peek(self) -> int:
        """
        Get the front element.

        Returns:
        int: The front element of the queue.
        """
        self.transfer_si_necessaire()
        return self.pile_sortie[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.

        Returns:
        bool: True if the queue is empty, False otherwise.
        """
        return not self.pile_entree and not self.pile_sortie

    def transfer_si_necessaire(self):
        """
        Transfers elements from the input stack to the output stack if necessary.
        """
        if not self.pile_sortie:
            while self.pile_entree:
                self.pile_sortie.append(self.pile_entree.pop())

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
