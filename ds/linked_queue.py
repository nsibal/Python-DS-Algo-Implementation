from ds.exception.empty import Empty
from ds.node import Node


class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""

    def __init__(self):
        """Create an empty queue."""
        self._head = None                       # reference to the head node
        self._tail = None                       # reference to the tail node
        self._size = 0                          # number of queue elements

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head.element               # front aligned with head of the list

    def dequeue(self):
        """Remove and return the first element of the queue (i.e. FIFO).

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        element = self._head.element
        self._head = self._head.next
        self._size -= 1
        if self._size == 0:                     # special case as queue is empty
            self._tail = None                   # removed head had been the tail
        return element

    def enqueue(self, e):
        """Add element e to the back of the queue."""
        node = Node(e, None)                    # node will be the new tail node
        if self.is_empty():
            self._head = node                   # special case: previously empty
        else:
            self._tail.next = node
        self._tail = node                       # update reference to tail node
        self._size += 1
