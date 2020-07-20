class Node:
    """Lightweight class for storing a singly linked node."""
    __slots__ = 'element', 'next'       # streamline memory usage

    def __init__(self, element, next):  # initialize node's fields
        self.element = element          # reference to user's element
        self.next = next                # reference to next node
