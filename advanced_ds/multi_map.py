class MultiMap:
    """A multimap class built upon use of an underlying map for storage."""
    _MapType = dict                                         # Map type; can be redefined by subclass

    def __init__(self):
        """Create a new empty multimap instance."""
        self._map = self._MapType()                         # create map instance for storage
        self._n = 0

    def __iter__(self):
        """Iterate through all (k, v) pairs in multimap."""
        for k, container in self._map.items():
            for v in container:
                yield (k, v)

    def add(self, k, v):
        """Add pair (k, v) to multimap."""
        container = self._map.setdefault(k, [])             # create empty list, if needed
        container.append(v)
        self._n += 1

    def pop(self, k):
        """Remove and return arbitrary (k, v) with key k.

        Raise KeyError if k is not in the map.
        """
        container = self._map[k]                            # may raise KeyError
        v = container.pop()
        if len(container) == 0:
            del self._map[k]                                # no pairs left
        self._n -= 1
        return (k, v)

    def find(self, k):
        """Return arbitrary (k, v) with key k.

        Raise KeyError if k is not in the map.
        """
        container = self._map[k]                            # may raise KeyError
        return (k, container[0])

    def find_all(self, k):
        """Generate iteration of all (k, v) pairs with key k."""
        container = self._map.get(k, [])                    # empty list, by default
        for v in container:
            yield (k, v)
