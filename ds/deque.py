from ds.exception.empty import Empty


class Deque:
    """Double Ended queue implementation using a Python list as underlying storage.

    Alternatively, deque class from _collections module can be used.
    """
    DEFAULT_CAPACITY = 10                                   # moderate capacity for all new queues

    def __init__(self):
        """Create an empty queue."""
        self._data = [None] * Deque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.

        _collections.deque()[0]
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def last(self):
        """Return (but do not remove) the element at the back of the queue.

        _collections.deque()[-1]
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        back = (self._front + self._size - 1) % len(self._data)
        return self._data[back]

    def add_first(self, e):
        """Add element e at the front of the queue.

        appendleft() in _collections.deque()
        """
        if self._size == len(self._data):
            self._resize(len(self._data) * 2)               # double the array size
        self._front = (self._front - 1) % len(self._data)   # cyclic shift
        self._data[self._front] = e
        self._size += 1

    def add_last(self, e):
        """Add element e to the back of the queue.

        Enqueue operation of the standard Queue.
        append() in _collections.deque()
        """
        if self._size == len(self._data):
            self._resize(len(self._data) * 2)               # double the array size
        available = (self._front + self._size) % len(self._data)
        self._data[available] = e
        self._size += 1

    def delete_first(self):
        """Remove and return the first element of the queue.

        Dequeue operation of the standard Queue.
        popleft() in _collections.deque()
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        element = self._data[self._front]
        self._data[self._front] = None                      # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        self._shrink()
        return element

    def delete_last(self):
        """Remove and return the last element of the queue.

        pop() in _collections.deque()
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        back = (self._front + self._size - 1) % len(self._data)
        element = self._data[back]
        self._data[back] = None                             # help garbage collection
        self._size -= 1
        self._shrink()
        return element

    def _resize(self, capacity):                            # we assume capacity >= len(self)
        """Resize to a new list of capacity >= len(self)."""
        existing_data = self._data                          # keep track of existing data
        self._data = [None] * capacity                      # allocate list with new capacity
        front = self._front
        for i in range(self._size):                         # only consider existing elements
            self._data[i] = existing_data[front]            # intentionally shift indices
            front = (front + 1) % len(existing_data)        # use existing list size as modulus
        self._front = 0                                     # front has been realigned

    def _shrink(self):
        """Reduce the array to half of its current size whenever the number of elements stored in it falls below 1/4th
        of its capacity.
        """
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
