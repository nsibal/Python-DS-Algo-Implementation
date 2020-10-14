"""
    BINARY SEARCH
"""


def binary_search(data, target, low, high):
    """
    Return True if target is found in indicated portion of the Python list.

    The search only considers the portion from data[low] to data[high] inclusive.
    """
    if low > high:
        return False                                        # interval is empty; no match
    mid = (low + high) // 2
    if target == data[mid]:                                 # found a match
        return True
    elif target < data[mid]:
        return binary_search(data, target, low, mid - 1)
    else:
        return binary_search(data, target, mid + 1, high)


def search(data, target):
    return binary_search(data, target, 0, len(data) - 1)


if __name__ == "__main__":
    seq = [12, 15, 18, 25, 36, 51]
    found = search(seq, 1)
    print(found)
