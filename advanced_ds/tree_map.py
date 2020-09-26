from advanced_ds.map_base import MapBase
from ds.linked_binary_tree import LinkedBinaryTree


class TreeMap(LinkedBinaryTree, MapBase):
    """Sorted map implementation using a binary search tree."""

    # --------------------------- override Position class ---------------------------
    class Position(LinkedBinaryTree.Position):
        def key(self):
            """Return key of map's key-value pair."""
            return self.element()._key

        def value(self):
            """Return value of map's key-value pair."""
            return self.element()._value

    # ----------------------------- nonpublic utilities -----------------------------
    def _subtree_search(self, p, k):
        """Return Position of p's subtree having key k, or last node searched."""
        if k == p.key():                                            # found match
            return p
        elif k < p.key():                                           # search left subtree
            if self.left(p) is not None:
                return self._subtree_search(self.left(p), k)
        else:                                                       # search right subtree
            if self.right(p) is not None:
                return self._subtree_search(self.right(p), k)
        return p                                                    # unsuccessful search

    def _subtree_first_position(self, p):
        """Return Position of first item in subtree rooted at p."""
        walk = p
        while self.left(walk) is not None:                          # keep walking left
            walk = self.left(walk)
        return walk

    def _subtree_last_position(self, p):
        """Return Position of last item in subtree rooted at p."""
        walk = p
        while self.right(walk) is not None:                         #  keep walking right
            walk = self.right(walk)
        return walk

    # ------------------------------- public methods -------------------------------
    def first(self):
        """Return the first Position in the tree (or None if empty)."""
        if len(self) <= 0:
            return None
        return self._subtree_first_position(self.root())

    def last(self):
        """Return the last Position in the tree (or None if empty)."""
        if len(self) <= 0:
            return None
        return self._subtree_last_position(self.root())

    def before(self, p):
        """Return the Position just before p in the natural order.

        Return None if p is the first position.
        """
        self._validate(p)                                           # inherited from LinedBinaryTree
        if self.left(p):
            return self._subtree_last_position(self.left(p))
        walk = p
        above = self.parent(p)                                      # walk upward
        while above is not None and walk == self.left(above):
            walk = above
            above = self.parent(walk)
        return above

    def after(self, p):
        """Return the Position just after p in the natural order.

        Return None if p is the last position.
        """
        self._validate(p)                                           # inherited from LinedBinaryTree
        if self.right(p):
            return self._subtree_first_position(self.right(p))
        walk = p
        above = self.parent(p)                                      # walk upward
        while above is not None and walk == self.right(above):
            walk = above
            above = self.parent(walk)
        return above

    def find_position(self, k):
        """Return position with key k, or else neighbor (or None if empty)."""
        if self.is_empty():
            return None
        p = self._subtree_search(self.root(), k)
        self._rebalance_access(p)                                   # hook for balanced tree subclass
        return p

    def find_min(self):
        """Return (key, value) pair with minimum key (or None if empty)."""
        if self.is_empty():
            return None
        p = self.first()
        return (p.key(), p.value())

    def find_ge(self, k):
        """Return (key, value) pair with least key greater than or equal to k.

        Return None if there does not exist such a key.
        """
        if self.is_empty():
            return None
        p = self.find_position(k)                                   # may not find exact match
        if p.key() < k:                                             # p's key is smaller than k
            p = self.after(p)
        return (p.key(), p.value()) if p is not None else None

    def find_range(self, start, stop):
        """Iterate all (key, value) pairs such that start <= key < stop.

        If start is None, iteration begins with minimum key of the map.
        If stop is None, iteration continues through the maximum key of map.
        """
        if self.is_empty():
            return None
        if start is None:
            p = self.first()
        else:
            p = self.find_position(start)
            if p.key() < start:
                p = self.after(p)
        while p is not None and (stop is None or p.key() < stop):
            yield (p.key(), p.value())
            p = self.after(p)

    def __getitem__(self, item):
        """Return value associated with key item.

        Raise KeyError if not found.
        """
        if self.is_empty():
            raise KeyError('Key Error: ' + repr(item))
        p = self._subtree_search(self.root(), item)
        self._rebalance_access(p)                                   # hook for balanced tree subclasses
        if item != p.key():
            raise KeyError('Key Error: ' + repr(item))
        return p.value()

    def __setitem__(self, key, value):
        """Assign value to key, overwriting existing value if present."""
        if self.is_empty():
            leaf = self._add_root(self._Item(key, value))
        else:
            p = self._subtree_search(self.root(), key)
            if p.key() == key:
                p.element()._value = value                          # replace existing item's value
                self._rebalance_access(p)                           # hook for balanced tree subclass
                return
            item = self._Item(key, value)
            if p.key() < key:
                leaf = self._add_right(p, item)                     # inherited from LinkedBinaryTree
            else:
                leaf = self._add_left(p, item)                      # inherited from LinkedBinaryTree
        self._rebalance_insert(leaf)                                # hook for balanced tree subclass

    def __iter__(self):
        """Generate an iteration of all keys in the map in order."""
        p = self.first()
        while p is not None:
            yield p.key()
            p = self.after(p)

    def delete(self, p):
        """Remove the item at given Position."""
        self._validate(p)                                           # inherited from LinkedBinaryTree
        if self.left(p) and self.right(p):                          # p has two children
            replacement = self._subtree_last_position(self.left(p))
            self._replace(p, replacement.element())                 # inherited from LinkedBinaryTree
            p = replacement                                         # now p has at most one child
        parent = self.parent(p)
        self._delete(p)                                             # inherited from LinkedBinaryTree
        self._rebalance_delete(parent)                              # if root is deleted, parent is None

    def __delitem__(self, key):
        """Remove item associated with key.

        Raise KeyError if not found.
        """
        if not self.is_empty():
            p = self._subtree_search(self.root(), key)
            if p.key() == key:
                self.delete(p)                                      # rely on positional version
                return                                              # successful deletion complete
            self._rebalance_access(p)                               # hook for balanced tree subclass
        raise KeyError('Key Error: ' + repr(key))

    def _rebalance_insert(self, p): pass

    def _rebalance_delete(self, p): pass

    def _rebalance_access(self, p): pass
