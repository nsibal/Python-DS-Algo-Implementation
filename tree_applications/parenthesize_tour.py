from ds.linked_tree import LinkedTree
from tree_applications.euler_tour import EulerTour


class Parenthesize(EulerTour):
    """
        Prints the tree's elements in preorder fashion with children of node enclosed in a set of braces Eg.:

        Electronics R'Us (R&D (Domestic, International), Sales (North America (US, Canada, Mexico),
        Asia (India, China, Pakistan)))
    """

    def _hook_previsit(self, p, d, path):
        if path and path[-1] > 0:                               # p follows a sibling
            print(', ', end='')                                 # so preface with comma
        print(p.element(), end='')                              # then print element
        if self.tree().is_leaf(p):
            return
        print(' (', end='')                                     # print opening parenthesis if p has children

    def _hook_postvisit(self, p, d, path, results):
        if self.tree().is_leaf(p):
            return
        print(')', end='')


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
    tour = Parenthesize(tree)
    tour.execute()
