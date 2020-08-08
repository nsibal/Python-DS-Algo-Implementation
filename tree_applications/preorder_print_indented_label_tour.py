from ds.linked_tree import LinkedTree
from tree_applications.euler_tour import EulerTour


class PreorderPrintIndentedLabelTour(EulerTour):
    """
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

    def _hook_previsit(self, p, d, path):
        label = '.'.join(str(j + 1) for j in path)              # displayed labels are one-indexed
        print(4 * d * ' ' + label, p.element())


if __name__ == "__main__":
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
    tour = PreorderPrintIndentedLabelTour(tree)
    tour.execute()
