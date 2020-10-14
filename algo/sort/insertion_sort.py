"""
    INSERTION SORT:
    The element is INSERTED to its right position.
    We just compare the element with the prev element and not with the entire prev subarray.

    Pseudo Code:
    Start with the first element. It is sorted by itself.
    Go to the second element:
        If it is smaller than the first, SWAP it with the first
        Else, leave it there.
    Go to the third:
        FIND its right place and place it there by moving items
        Current item moves only once...
"""


def insertion_sort(lst):
    for i in range(1, len(lst)):                    # from 1 to n-1
        curr = lst[i]                               # current element to be inserted
        j = i                                       # find correct index j for current
        while j > 0 and lst[j - 1] > curr:          # element lst[j-1] must be after current
            lst[j] = lst[j-1]
            j -= 1
        lst[j] = curr                               # curr is now in the right place


if __name__ == "__main__":
    seq = [12, 11, 13, 5, 6, 1]
    insertion_sort(seq)
    print(seq)
