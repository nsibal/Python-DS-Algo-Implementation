from advanced_ds.hash_map_base import HashMapBase
from advanced_ds.unsorted_table_map import UnsortedTableMap


class ChainHashMap(HashMapBase):
    """Hash map implemented with separate chaining for collision resolution."""

    def _bucket_getitem(self, index, key):
        bucket = self._table[index]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(key))           # no match found
        return bucket[key]                                      # may raise KeyError

    def _bucket_setitem(self, index, key, value):
        if self._table[index] is None:
            self._table[index] = UnsortedTableMap()             # bucket is new of the table
        oldsize = len(self._table[index])
        self._table[index][key] = value
        if len(self._table[index]) > oldsize:                   # key was new to the table
            self._n += 1                                        # increase overall map size

    def _bucket_delitem(self, index, key):
        bucket = self._table[index]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(key))           # no match found
        del bucket[key]                                         # may raise KeyError

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:                              # a nonempty slot
                for key in bucket:
                    yield key
