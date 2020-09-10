from advanced_ds.priority_queue_base import PriorityQueueBase
from exception.empty import Empty


class HeapPriorityQueue(PriorityQueueBase):                             # base class defines _Item
    """A min-oriented priority queue implemented with a binary heap."""

    # ---------------------------- nonpublic behaviors ----------------------------
    def _parent(self, j):
        return (j-1) // 2

    def _left(self, j):
        return 2*j + 1

    def _right(self, j):
        return 2*j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)                          # index beyond end of list?

    def _has_right(self, j):
        return self._right(j) < len(self._data)                         # index beyond end of list?

    def _swap(self, i, j):
        """Swap the elements at indices i and j of array."""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)                                        # recur at position of parent

    def _downheap(self, j):
        if not self._has_left(j):
            # since we are dealing with indexes of an array, it won't be possible for an array to have
            # a right without having a left because index of right > index of left.
            return
        left = self._left(j)
        small_child = left                                              # although right may be smaller
        if self._has_right(j):
            right = self._right(j)
            if self._data[right] < self._data[left]:
                small_child = right
        if self._data[small_child] < self._data[j]:
            self._swap(j, small_child)
            self._downheap(small_child)                                 # recur at position of small child

    def _heapify(self):
        start = self._parent(len(self._data) - 1)                       # start at the PARENT of the last leaf
        for j in range(start, -1, -1):                                  # going to and including the root
            self._downheap(j)

    # ------------------------------ public behaviors ------------------------------
    def __init__(self, contents=()):
        """Create a new Priority Queue

        By default, queue will be empty. If contents is given, it should be as an
        iterable sequence of (k,v) tuples specifying the initial contents.
        """
        self._data = [self._Item(k, v) for k, v in contents]            # empty by default
        if len(self._data) > 1:
            self._heapify()

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair to the priority queue."""
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1)                               # upheap newly added position

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key.

        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Priority Queue is empty')
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key.

        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Priority Queue is empty')
        self._swap(0, len(self._data) - 1)                              # put minimum item at the end
        item = self._data.pop()                                         # and remove it from the list
        self._downheap(0)                                               # then fix new root
        return (item._key, item._value)
