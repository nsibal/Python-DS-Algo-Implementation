from ds.exception.empty import Empty


class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10                               # moderate capacity for all new queues

    def __init__(self):
        """Create an empty queue."""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
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

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        """Remove and return the first element of the queue (i.e. FIFO).

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        element = self._data[self._front]
        self._data[self._front] = None                  # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        self._shrink()
        return element

    def enqueue(self, e):
        """Add element e to the back of the queue."""
        if self._size == len(self._data):
            self._resize(len(self._data) * 2)           # double the array size
        available = (self._front + self._size) % len(self._data)
        self._data[available] = e
        self._size += 1

    def _resize(self, capacity):                        # we assume capacity >= len(self)
        """Resize to a new list of capacity >= len(self)."""
        existing_data = self._data                      # keep track of existing data
        self._data = [None] * capacity                  # allocate list with new capacity
        front = self._front
        for i in range(self._size):                     # only consider existing elements
            self._data[i] = existing_data[front]        # intentionally shift indices
            front = (front + 1) % len(existing_data)    # use existing list size as modulus
        self._front = 0                                 # front has been realigned

    def _shrink(self):
        """Reduce the array to half of its current size whenever the number of elements stored in it falls below 1/4th
        of its capacity.
        """
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
