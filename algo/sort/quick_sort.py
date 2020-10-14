"""
    QUICK SORT:
    Uses Divide-and-Conquer approach.
    Selects a pivot element (usually the last element of the list) and then
    traverses the sub array and arranges elements such that all the elements
    less than pivot are separated from all the elements greater than pivot.
    And then performs the same operation recursively.

    Pseudo Code:
    Select the last element of the subarray as pivot.
    Move elements in the subarray such that:
        all the elements in the array [:i] are less than pivot
        all the elements in the array [i:] are greater than or equal to pivot
    Move pivot to its position.
    Recursively solve the two subarrays.
"""


def partition(lst, low, high):
    i = low - 1                                         # index of smaller element
    pivot = lst[high]
    for j in range(low, high):
        if lst[j] < pivot:
            # if current element is smaller than the pivot
            # replace this element with the element next to
            # the last element smaller than pivot
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i + 1], lst[high] = lst[high], lst[i + 1]       # replace pivot with the first element bigger than pivot
    return i + 1


def sort_sublist(lst, low, high):
    if low >= high:
        return
    pi = partition(lst, low, high)                      # pi is the index of the element that is now sorted
    sort_sublist(lst, low, pi - 1)                      # sort all the elements less than lst[pi]
    sort_sublist(lst, pi + 1, high)                     # sort all the elements greater than lst[pi]


def quick_sort(lst):
    sort_sublist(lst, 0, len(lst)-1)


if __name__ == "__main__":
    seq = [12, 11, 13, 5, 6, 1]
    quick_sort(seq)
    print(seq)
