"""
    BUBBLE SORT:
    Sort bubbles (pairs of two) n times.

    Pseudo Code:
    Repeat n times:
        For each element:
            if current > next:
                swap (current, next)
"""


def bubble_sort(lst):
    for i in range(len(lst)):                               # repeat n times
        for j in range(len(lst) - 1):                       # for each element
            if lst[j] > lst[j + 1]:                         # if current > next
                lst[j], lst[j + 1] = lst[j + 1], lst[j]     # swap


if __name__ == "__main__":
    seq = [12, 11, 13, 5, 6, 1]
    bubble_sort(seq)
    print(seq)
