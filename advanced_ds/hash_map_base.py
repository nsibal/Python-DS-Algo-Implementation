from random import randrange
from advanced_ds.map_base import MapBase


class HashMapBase(MapBase):
    """Abstract base class for map using hash-table with MAD compression."""

    def __init__(self, cap=11, p=109345121):
        """Create an empty hash-table map."""
        self._table = cap * [None]
        self._n = 0                                             # number of entries in the map
        self._prime = p                                         # prime for MAD compression
        self._scale = 1 + randrange(p - 1)                      # scale from 1 to p-1 for MAD
        self._shift = randrange(p)                              # shift from 0 to p-1 for MAD

    def _hash_function(self, k):
        """Uses the MAD formula: [((ai + b) % p) % N]"""
        return (((self._scale * hash(k)) + self._shift) % self._prime) % len(self._table)

    def __len__(self):
        return self._n

    def __getitem__(self, item):
        j = self._hash_function(item)
        return self._bucket_getitem(j, item)                    # may raise KeyError

    def __setitem__(self, key, value):
        j = self._hash_function(key)
        self._bucket_setitem(j, key, value)                     # subroutine maintains self._n
        if self._n > len(self._table) // 2:                     # keep load factor <= 0.5
            self._resize(2 * len(self._table) - 1)              # number 2*x-1 is often prime

    def __delitem__(self, key):
        j = self._hash_function(key)
        self._bucket_delitem(j, key)                            # may raise KeyError
        self._n -= 1

    def _resize(self, c):                                       # resize bucket array to capacity c
        old = list(self.items())                                # uses iteration to record existing items
        self._table = c * [None]                                # then reset table to desired capacity
        self._n = 0                                             # n will be recomputed during subsequent adds
        for (k, v) in old:
            self[k] = v                                         # reinsert old key-value pair
