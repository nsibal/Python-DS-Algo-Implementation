"""
    MERGE SORT:
    Uses Divide-and-Conquer approach.
    Divides the list into two sorted lists, and then merges them.

    Pseudo Code:
    Divide the list into two halves.
    Sort those two halves.
    Merge those two.
"""


def merge(lst1, lst2, lst):
    """Merge the two sorted lists lst1 and lst2 into properly sized list lst."""
    i = j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            lst[i + j] = lst1[i]    # copy ith element of lst1 as next item of lst
            i += 1
        else:
            lst[i + j] = lst2[j]    # copy jth element of lst2 as next item of lst
            j += 1

    while i < len(lst1):            # adding the remaining elements of lst1 if any
        lst[i + j] = lst1[i]
        i += 1

    while j < len(lst2):            # adding the remaining elements of lst2 if any
        lst[i + j] = lst2[j]
        j += 1


def merge_sort(lst):
    n = len(lst)
    if n < 2:                       # lst is already sorted
        return
    # divide
    mid = n // 2
    lst1 = lst[:mid]                # make a copy of first half
    lst2 = lst[mid:]                # make a copy of second half
    # conquer (with recursion)
    merge_sort(lst1)                # sort the copy of first half
    merge_sort(lst2)                # sort the copy of second half
    merge(lst1, lst2, lst)          # merge the sorted halves back into lst


if __name__ == "__main__":
    seq = [12, 11, 13, 5, 6, 1]
    merge_sort(seq)
    print(seq)
