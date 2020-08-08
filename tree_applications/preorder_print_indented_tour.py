from ds.linked_tree import LinkedTree
from tree_applications.euler_tour import EulerTour


class PreorderPrintIndentedTour(EulerTour):
    """
        Prints the tree's elements in preorder fashion with children of a node indented. Eg:
        1
            2
                3
                4
            5
                6
    """

    def _hook_previsit(self, p, d, path):
        print(4*d*' ' + str(p.element()))


if __name__ == "__main__":
    tree = LinkedTree()
    root_p = tree._add_root(1)
    root_child_p1 = tree._add_child(root_p, 2)
    tree._add_child(root_child_p1, 3)
    tree._add_child(root_child_p1, 4)
    root_child_p2 = tree._add_child(root_p, 5)
    tree._add_child(root_child_p2, 6)
    tour = PreorderPrintIndentedTour(tree)
    tour.execute()
