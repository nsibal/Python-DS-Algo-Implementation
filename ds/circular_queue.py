from ds.exception.empty import Empty
from ds.node import Node


class CircularQueue:
    """Queue implementation using circularly linked list for storage."""

    def __init__(self):
        """Create an empty queue."""
        self._tail = None                       # will represent tail of queue
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
        head = self._tail.next
        return head.element

    def dequeue(self):
        """Remove and return the first element of the queue (i.e. FIFO).

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        oldhead = self._tail.next
        if self._size == 1:                     # removing only element
            self._tail = None                   # queue becomes empty
        else:
            self._tail.next = oldhead.next      # bypass the old head
        self._size -= 1
        return oldhead.element

    def enqueue(self, e):
        """Add element e to the back of the queue."""
        newest = Node(e, None)                  # node will be the new tail node
        if self.is_empty():
            newest.next = newest                # initialize circularly
        else:
            newest.next = self._tail.next       # new node points to head
            self._tail.next = newest            # old tail points to new node
        self._tail = newest                     # new node becomes the tail
        self._size += 1

    def rotate(self):
        """Rotate front elements to the back of the queue."""
        if self._size > 0:
            self._tail = self._tail.next        # old heads becomes new tail
