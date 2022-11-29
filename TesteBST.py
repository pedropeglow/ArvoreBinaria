import unittest
from BinarySearchTree import BinarySearchTree


class TestMainTest(unittest.TestCase):

    def remove_element(self, label):
        print("Arvore antes da remocao")
        self.tree.showTree(self.tree.getRoot(), self.tree.getRoot())
        print("")
        print("Elemento a ser removido:", label)
        self.tree.removeNovo(label)
        print("")
        print("Arvore depois da remocao")
        self.tree.showTree(self.tree.getRoot(), self.tree.getRoot())

    def setUp(self):

        self.show = True
        self.tree = BinarySearchTree()

        self.tree.insert(9)
        self.tree.insert(3)
        self.tree.insert(2)
        self.tree.insert(1)
        self.tree.insert(4)
        self.tree.insert(5)
        self.tree.insert(21)
        self.tree.insert(25)
        self.tree.insert(29)
        self.tree.insert(23)
        self.tree.insert(24)
        self.tree.insert(31)

    def test_remove_nodo_folha(self):
        if self.show:
            self.remove_element(31)
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
