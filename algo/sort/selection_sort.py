"""
    SELECTION SORT:
    The minimum element is SELECTED from the unsorted part of the list and placed at the end of the sorted part.
    We compare the element with the whole sublist starting immediately after the element.

    Pseudo Code:
    For each element:
        Look for the smallest element in the sublist starting immediately after that element.
        Replace these two elements with each other.
"""


def selection_sort(lst):
    for i in range(len(lst)):                           # for each element
        min_idx = i                                     # find the minimum element
        for j in range(i+1, len(lst)):                  # in the remaining unsorted list
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]     # replace the element with the min


if __name__ == "__main__":
    seq = [12, 11, 13, 5, 6, 1]
    selection_sort(seq)
    print(seq)
