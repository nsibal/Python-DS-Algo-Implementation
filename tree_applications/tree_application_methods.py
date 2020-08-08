from ds.linked_tree import LinkedTree

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


def print_preorder():
    tree = LinkedTree()
    root_p = tree._add_root(1)
    root_child_p1 = tree._add_child(root_p, 2)
    tree._add_child(root_child_p1, 3)
    tree._add_child(root_child_p1, 4)
    root_child_p2 = tree._add_child(root_p, 5)
    tree._add_child(root_child_p2, 6)
    print("\n ===== Pre-order Print: ===== ")
    for p in tree.preorder():
        print(p.element())


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


def preorder_indent(t, p, d):
    """Print preorder representation of subtree of Tree t rooted at Position p at Depth d."""
    print(4 * d * ' ' + str(p.element()))  # use depth for indentation
    for c in t.children(p):
        preorder_indent(t, c, d + 1)  # child depth is d+1


def print_preorder_indent():
    tree = LinkedTree()
    root_p = tree._add_root(1)
    root_child_p1 = tree._add_child(root_p, 2)
    tree._add_child(root_child_p1, 3)
    tree._add_child(root_child_p1, 4)
    root_child_p2 = tree._add_child(root_p, 5)
    tree._add_child(root_child_p2, 6)
    print("\n ===== Pre-order Indent Print: ===== ")
    preorder_indent(tree, tree.root(), 0)


"""
    PREORDER LABEL:
    Prints the tree's elements in preorder fashion with children of a node indented and
    numbered in the following format:

    Electronics R'Us
        1 R&D
            1.1 Domestic
            1.2 International
        2 Sales
            2.1 North America
                2.1.1 US
                2.1.2 Canada
                2.1.3 Mexico
            2.2 Asia
                2.2.1 India
                2.2.2 China
                2.2.3 Pakistan
"""


def preorder_label(t, p, d, path):
    """Print labeled representation of subtree of Tree t rooted at Position p at Depth d."""
    label = '.'.join(str(j + 1) for j in path)  # displayed labels are one-indexed
    print(4 * d * ' ' + label, p.element())
    path.append(0)  # path entries are zero-indexed
    for c in t.children(p):
        preorder_label(t, c, d + 1, path)  # child depth is d+1
        path[-1] += 1
    path.pop()


def print_preorder_label():
    tree = LinkedTree()
    root_p = tree._add_root("Electronics R\'Us")
    root_child_p1 = tree._add_child(root_p, "R&D")
    root_child_p2 = tree._add_child(root_p, "Sales")
    tree._add_child(root_child_p1, "Domestic")
    tree._add_child(root_child_p1, "International")
    p1_child_q1 = tree._add_child(root_child_p2, "North America")
    p1_child_q2 = tree._add_child(root_child_p2, "Asia")
    for i in ["US", "Canada", "Mexico"]:
        tree._add_child(p1_child_q1, i)
    for i in ["India", "China", "Pakistan"]:
        tree._add_child(p1_child_q2, i)
    print("\n ===== Pre-order Label Print: ===== ")
    preorder_label(tree, tree.root(), 0, [])


"""
    PARENTHESIZE:
    Prints the tree's elements in preorder fashion with children of node enclosed in a set of braces Eg.:

    Electronics R'Us (R&D (Domestic, International), Sales (North America (US, Canada, Mexico),
    Asia (India, China, Pakistan)))
"""


def parenthesize(t, p):
    """Print parenthesized representation of subtree of Tree t rooted at Position p."""
    print(p.element(), end='')  # use of end avoids trailing newline
    if t.is_leaf(p):
        return
    first_time = True
    for c in t.children(p):
        sep = ' (' if first_time else ', '  # determine proper separator
        print(sep, end='')
        first_time = False  # any future passes will not be the first
        parenthesize(t, c)  # recur on child
    print(')', end='')  # include closing parenthesis


def print_parenthesize():
    tree = LinkedTree()
    root_p = tree._add_root("Electronics R\'Us")
    root_child_p1 = tree._add_child(root_p, "R&D")
    root_child_p2 = tree._add_child(root_p, "Sales")
    tree._add_child(root_child_p1, "Domestic")
    tree._add_child(root_child_p1, "International")
    p1_child_q1 = tree._add_child(root_child_p2, "North America")
    p1_child_q2 = tree._add_child(root_child_p2, "Asia")
    for i in ["US", "Canada", "Mexico"]:
        tree._add_child(p1_child_q1, i)
    for i in ["India", "China", "Pakistan"]:
        tree._add_child(p1_child_q2, i)
    print("\n ===== Parenthesized Print: ===== ")
    parenthesize(tree, tree.root())


if __name__ == "__main__":
    print_preorder()
    print_preorder_indent()
    print_preorder_label()
    print_parenthesize()
