"""
    HEAP SORT (in place):
    Given a list of elements, we perform heap sort in two phases:
        Phase 1: Build Heap:
                 Arrange the elements in the list itself according to the MAX heap fashion.
        Phase 2: Extraction:
                 Extract the maximum of the heap (i.e, the root of the tree or 0th index of the list).
                 Put it at the n-i th position.

    The resulting list will be sorted in ascending order.

    A list is Heap when if element at index i is a root, then 2*i+1 and 2*i+2 are its left and right
    children respectively.
"""


def heapify(arr, n, i):
    root = i                                                    # root should be the largest
    left_child = 2 * i + 1                                      # left = 2*i + 1
    right_child = 2 * i + 2                                     # right = 2*i + 2

    # See if left child of root exists and is greater than root
    if left_child < n and arr[root] < arr[left_child]:
        root = left_child

    # See if right child of root exists and is greater than root
    if right_child < n and arr[root] < arr[right_child]:
        root = right_child

    if root != i:                                               # If root was less than left or right child
        arr[i], arr[root] = arr[root], arr[i]                   # swap
        heapify(arr, n, root)                                   # heapify the root


def remove_max(arr, i):
    # max is always at the root (0th index in case of an array)
    arr[i], arr[0] = arr[0], arr[i]


def build_heap(arr):
    n = len(arr)
    last_non_leaf = n // 2 - 1                                  # start arranging from the PARENT of the leaf node
    for i in range(last_non_leaf, -1, -1):
        heapify(arr, n, i)


def extraction(arr):
    n = len(arr)
    for i in range(n-1, 0, -1):
        remove_max(arr, i)                                      # remove maximum
        heapify(arr, i, 0)                                      # arrange the heap to maintain heap order


def heap_sort(arr):
    build_heap(arr)                                             # phase 1
    extraction(arr)                                             # phase 2


if __name__ == "__main__":
    seq = [10, 2, 7, 55, 99, 16, 4, 32, 12]
    heap_sort(seq)
    print(seq)
