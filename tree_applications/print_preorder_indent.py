"""
    PREORDER INDENT:
    Prints the tree's elements in preorder fashion with children of a node indented. Eg:
    1
        2
            3
            4
        5
            6
"""

from ds.linked_tree import LinkedTree


def preorder_indent(t, p, d):
    """Print preorder representation of subtree of Tree t rooted at Position p at Depth d."""
    print(2*d*' ' + str(p.element()))       # use depth for indentation
    for c in t.children(p):
        preorder_indent(t, c, d+1)          # child depth is d+1


def print_preorder_indent(tree):
    preorder_indent(tree, tree.root(), 0)


if __name__ == "__main__":
    tree = LinkedTree()
    root_p = tree._add_root(1)
    root_child_p1 = tree._add_child(root_p, 2)
    tree._add_child(root_child_p1, 3)
    tree._add_child(root_child_p1, 4)
    root_child_p2 = tree._add_child(root_p, 5)
    tree._add_child(root_child_p2, 6)
    print_preorder_indent(tree)
