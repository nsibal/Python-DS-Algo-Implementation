from advanced_ds.favorites_list import FavoritesList
from ds.positional_list import PositionalList


class FavoritesListMTF(FavoritesList):
    """List of elements ordered with move-to-front heuristic.

    Commonly known as Self Organizing List (Move To Front Method)
    """

    # we override _move_up to provide move-to-front semantics
    def _move_up(self, p):
        """Move accessed item at Position p to front of list."""
        if p != self._data.first():
            element = self._data.delete(p)              # delete the item at p
            self._data.add_first(element)               # reinsert at the front

    # we override top because list is no longer sorted
    def top(self, k):
        """Generate sequence of top k elements in terms of access counts."""
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k')

        # we begin by making a copy of the original list
        temp = PositionalList()
        for item in self._data:                         # positional list supports iteration
            temp.add_last(item)

        # we repeatedly find, report, and remove element with the largest count
        for j in range(k):
            # find and report next highest from temp
            high_position = temp.first()
            walk = temp.after(high_position)
            while walk is not None:
                if walk.element()._count > high_position.element()._count:
                    high_position = walk
                walk = temp.after(walk)
            # we have found the element with the highest count
            yield high_position.element()._value        # report element to the user
            temp.delete(high_position)                  # remove from temp list
