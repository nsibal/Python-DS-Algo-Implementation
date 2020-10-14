"""
    LINEAR SEARCH
"""


def linear_search(data, target):
    for i in data:
        if i == target:
            return True
    return False


def search(data, target):
    return linear_search(data, target)


if __name__ == "__main__":
    seq = [12, 15, 18, 25, 36, 51]
    found = search(seq, 1)
    print(found)
