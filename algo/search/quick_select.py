"""
    RANDOMIZED QUICK SELECT
    Works on Prune-and-Search or Decrease-and-Conquer pattern.
    Used to find kth smallest element in an unordered list of elements.

    Pseudo Code:
    Pick a random pivot.
    Divide the list into three groups:
        L with elements < pivot
        E with elements = pivot
        G with elements > pivot
    Now based on the sizes of these three lists, you will find the kth element
    in either of these.
"""
import random


def randomized_quick_select(data, k):
    """Return the kth smallest element of list data. for k from 1 to len(data)."""
    if len(data) == 1:
        return data[0]
    pivot = random.choice(data)                             # pick random pivot element from data
    L = [i for i in data if i < pivot]                      # elements less than pivot
    E = [i for i in data if i == pivot]                     # elements equal to pivot
    G = [i for i in data if i > pivot]                      # elements greater than pivot
    if k <= len(L):
        return randomized_quick_select(L, k)                # kth smallest lies in L
    elif k <= len(L) + len(E):
        return pivot                                        # kth smallest is equal to pivot
    else:
        j = k - len(L) - len(E)                             # new selection parameter
        return randomized_quick_select(G, j)                # kth smallest is jth in G


if __name__ == "__main__":
    seq = [12, 15, 18, 25, 36, 51]
    k = 3
    kth_smallest = randomized_quick_select(seq, k)
    print(kth_smallest)
