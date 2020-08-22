from advanced_ds.hash_map_base import HashMapBase


class ProbeHashMap(HashMapBase):
    """Hash map implemented with linear probing for collision resolution."""
    _AVAIL = object()                                           # sentinel marks locations of previous deletions

    def _is_available(self, index):
        """Return True if index is available in table."""
        return self._table[index] is None or self._table[index] is ProbeHashMap._AVAIL

    def _find_slot(self, index, key):
        """Search for key in bucket at index.

        Return (success, index) tuple, described as follows:
        If match was found, success is True and index denotes its location.
        If no match found, success is False and index denotes first available slot.
        """
        firstAvail = None
        while True:
            if self._is_available(index):
                if firstAvail is None:
                    firstAvail = index                          # mark this as first available
                if self._table[index] is None:
                    return False, firstAvail                    # search has failed
            elif key == self._table[index]._key:
                return True, index                              # found a match
            index = (index + 1) % len(self._table)              # keep looking (cyclically)

    def _bucket_getitem(self, index, key):
        found, slot = self._find_slot(index, key)
        if not found:
            raise KeyError('Key Error: ' + repr(key))           # no match found
        return self._table[slot]._value

    def _bucket_setitem(self, index, key, value):
        found, slot = self._find_slot(index, key)
        if not found:
            self._table[slot] = self._Item(key, value)          # insert new item
            self._n += 1                                        # size has increased
        else:
            self._table[slot]._value = value                    # overwrite existing

    def _bucket_delitem(self, index, key):
        found, slot = self._find_slot(index, key)
        if not found:
            raise KeyError('Key Error: ' + repr(key))           # no match found
        self._table[slot] = ProbeHashMap._AVAIL                 # mark as vacated

    def __iter__(self):
        for index in range(len(self._table)):                   # scan entire table
            if not self._is_available(index):
                yield self._table[index]._key
