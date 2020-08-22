from advanced_ds.map_base import MapBase


class UnsortedTableMap(MapBase):
    """Map implementation using an unordered list."""

    def __init__(self):
        """Create an empty map."""
        self._table = []                                    # list of objects of _Item

    def __getitem__(self, item):
        """Return value associated with key k (raise KeyError if not found)."""
        for element in self._table:
            if item == element._key:
                return element._value
        raise KeyError('Key Error: ' + repr(item))

    def __setitem__(self, key, value):
        """Assign value to key overwriting existing value if present."""
        for element in self._table:
            if key == element._key:                         # Found a match:
                element._value = value                      # reassign a value
                return                                      # and quit
        # did not find match for key
        self._table.append(self._Item(key, value))

    def __delitem__(self, key):
        """Remove item associated with key (raise KeyError if not found)."""
        for j in range(len(self._table)):
            if key == self._table[j]._key:                  # Found a match:
                self._table.pop(j)                          # remove item
                return                                      # and quit
        raise KeyError('Key Error: ' + repr(key))

    def __len__(self):
        """Return number of items in the map."""
        return len(self._table)

    def __iter__(self):
        """Generate iteration of the map's keys."""
        for item in self._table:
            yield item._key                                 # yield the KEY
