import ctypes


class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""

    def __init__(self):
        """Create an empty array."""
        self._n = 0                                         # count actual element
        self._capacity = 1                                  # default array capacity
        self._A = self._make_array(self._capacity)          # low level array

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n

    def __getitem__(self, item):
        """Return element at index item."""
        if 0 <= item < self._n:
            raise IndexError('invalid index')
        return self._A[item]                                # retrieve from array

    def append(self, obj):
        """Add obj to end of the array."""
        if self._n == self._capacity:                       # not enough room
            self._resize(2 * self._capacity)                # so double capacity
        self._A[self._n] = obj
        self._n += 1

    def extend(self, other):
        """Extends the dynamic array by appending all the elements of other."""
        for element in other:
            self.append(element)

    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward."""
        # for simplicity, we assume that 0 <= k <= n in this version.
        if self._n == self._capacity:                       # not enough room
            self._resize(2 * self._capacity)                # so double capacity
        for j in range(self._n, k, -1):                     # shifting rightmost first
            self._A[j] = self._A[j-1]
        self._A[k] = value                                  # store newest element
        self._n += 1

    def remove(self, value):
        """Remove first occurrence of value (or raise ValueError)"""
        # note: we do not consider shrinking the dynamic array in this version
        for k in range(self._n):
            if self._A[k] == value:                         # found a match
                for j in range(k, self._n, -1):             # shift others to fill gap
                    self._A[j] = self._A[j+1]
                self._A[self._n - 1] = None                 # help garbage collection
                self._n -= 1                                # we have one less item
                return                                      # exit immediately
        raise ValueError('value not found')                 # only reached if no match

    def _resize(self, c):                                   # nonpublic utility
        """Resize internal array to capacity c."""
        B = self._make_array(c)                             # new (bigger) array
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B                                         # use the bigger array
        self._capacity = c

    def _make_array(self, c):                               # nonpublic utility
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()
