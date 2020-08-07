"""
    PRINT PREORDER:
    Prints the tree's elements in preorder fashion with one element per line. Eg:
    1
    2
    3
    4
    5
    6
"""

from ds.linked_tree import LinkedTree


def print_preorder(tree):
    for p in tree.preorder():
        print(p.element())


if __name__ == "__main__":
    tree = LinkedTree()
    root_p = tree._add_root(1)
    root_child_p1 = tree._add_child(root_p, 2)
    tree._add_child(root_child_p1, 3)
    tree._add_child(root_child_p1, 4)
    root_child_p2 = tree._add_child(root_p, 5)
    tree._add_child(root_child_p2, 6)
    print_preorder(tree)
