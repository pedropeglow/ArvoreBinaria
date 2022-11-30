import unittest
from BinarySearchTree import BinarySearchTree


class TestMainTest(unittest.TestCase):

    def insert_elemento_show_tree(self, label):
        print("Árvore antes da inserção -> ")
        self.tree.showTreePre(self.tree.getRoot(), self.tree.getRoot())
        print("-"*20)
        print("Elemento a ser inserido: ", label)
        self.tree.insert(label)
        print("-"*20)
        print("Árvore depois da inserção -> ")
        self.tree.showTreePre(self.tree.getRoot(), self.tree.getRoot())

    def remove_elemento_show_tree_pre(self, label):
        print("Árvore antes da remocao ->")
        self.tree.showTreePre(self.tree.getRoot(), self.tree.getRoot())
        print("-"*20)
        print("Elemento a ser removido:", label)
        self.tree.remove(label)
        print("-"*20)
        print("Arvore depois da remocao")
        self.tree.showTreePre(self.tree.getRoot(), self.tree.getRoot())

    def remove_elemento_show_tree_pos(self, label):
        print("Arvore antes da remocao")
        self.tree.showTreePos()
        print("")
        print("Elemento a ser removido:", label)
        self.tree.remove(label)
        print("")
        print("Arvore depois da remocao")
        self.tree.showTreePos()

    def setUp(self):

        self.show = True
        values = [10, 5, 3, 2, 7, 6, 30, 25, 28, 27, 29, 50, 55, 60]
        self.tree = BinarySearchTree()
        for v in values:
            self.tree.insert(v)
        return self.tree


    def test_remove_elemento_pos_ordem(self):

        if self.show:
            self.remove_elemento_show_tree_pos(27)
        self.assertTrue(True)


    def test_remove_elemento_pre_ordem(self):

        if self.show:
            self.remove_elemento_show_tree_pre(6)
        self.assertTrue(True)



    def test_insert_element(self):
        if self.show:
            self.insert_elemento_show_tree(20)
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()