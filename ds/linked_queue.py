from exception.empty import Empty


class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""

    # -------------------------- nested Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'         # streamline memory usage

        def __init__(self, element, next):      # initialize node's fields
            self._element = element             # reference to user's element
            self._next = next                   # reference to next node

    # ---------------------------- queue methods ----------------------------
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
        return self._head._element              # front aligned with head of the list

    def dequeue(self):
        """Remove and return the first element of the queue (i.e. FIFO).

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        element = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self._size == 0:                     # special case as queue is empty
            self._tail = None                   # removed head had been the tail
        return element

    def enqueue(self, e):
        """Add element e to the back of the queue."""
        node = self._Node(e, None)              # node will be the new tail node
        if self.is_empty():
            self._head = node                   # special case: previously empty
        else:
            self._tail._next = node
        self._tail = node                       # update reference to tail node
        self._size += 1

    def merge_sort(self):
        """Sort the elements of this queue using the Merge Sort algorithm."""
        n = len(self)
        if n < 2:
            return                              # already sorted
        # divide
        q1 = LinkedQueue()
        q2 = LinkedQueue()
        while len(q1) < n // 2:                 # move the first n // 2 elements to q1
            q1.enqueue(self.dequeue())
        while not self.is_empty():              # move the rest to q2
            q2.enqueue(self.dequeue())
        # conquer (with recursion)
        q1.merge_sort()                         # sort first half
        q2.merge_sort()                         # sort second half
        # merge results
        self._merge(q1, q2)

    def _merge(self, q1, q2):
        """Merge two sorted queue instances q1 and q2 into self."""
        while not q1.is_empty() and not q2.is_empty():
            if q1.first() < q2.first():
                self.enqueue(q1.dequeue())
            else:
                self.enqueue(q2.dequeue())
        while not q1.is_empty():                # move the remaining elements of q1 if any
            self.enqueue(q1.dequeue())
        while not q2.is_empty():                # move the remaining elements of q2 if any
            self.enqueue(q2.dequeue())

    def quick_sort(self):
        """Sort the elements of this queue using the Quick Sort algorithm."""
        n = len(self)
        if n < 2:
            return                              # already sorted
        # divide
        p = self.first()                        # using first as arbitrary pivot
        L = LinkedQueue()
        E = LinkedQueue()
        G = LinkedQueue()
        while not self.is_empty():              # divide self into L, E, and G
            if self.first() < p:
                L.enqueue(self.dequeue())
            elif p < self.first():
                G.enqueue(self.dequeue())
            else:                               # first is equal to pivot
                E.enqueue(self.dequeue())
        # conquer (with recursion)
        L.quick_sort()                          # sort elements less than p
        G.quick_sort()                          # sort elements greater than p
        # concatenate results
        while not L.is_empty():
            self.enqueue(L.dequeue())
        while not E.is_empty():
            self.enqueue(E.dequeue())
        while not G.is_empty():
            self.enqueue(G.dequeue())
