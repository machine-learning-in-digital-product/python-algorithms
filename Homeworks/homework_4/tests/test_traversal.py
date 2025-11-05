import unittest
from traversal.src.bst import BST


class TestBSTTraversals(unittest.TestCase):
    def setUp(self):
        self.tree = BST()
        for x in [5, 3, 7, 2, 4, 6, 8]:
            self.tree.insert(x)

    def test_preorder(self):
        self.assertEqual(self.tree.preorder(),
                         [5, 3, 2, 4, 7, 6, 8])

    def test_postorder(self):
        self.assertEqual(self.tree.postorder(),
                         [2, 4, 3, 6, 8, 7, 5])

    def test_inorder(self):
        self.assertEqual(self.tree.inorder(),
                         [2, 3, 4, 5, 6, 7, 8])

    def test_reverse_preorder(self):
        self.assertEqual(self.tree.reverse_preorder(),
                         [5, 7, 8, 6, 3, 4, 2])

    def test_reverse_postorder(self):
        self.assertEqual(self.tree.reverse_postorder(),
                         [8, 6, 7, 4, 2, 3, 5])

    def test_reverse_inorder(self):
        self.assertEqual(self.tree.reverse_inorder(),
                         [8, 7, 6, 5, 4, 3, 2])

    def test_single_node(self):
        t = BST()
        t.insert(42)
        expected = [42]
        self.assertEqual(t.preorder(), expected)
        self.assertEqual(t.postorder(), expected)
        self.assertEqual(t.inorder(), expected)
        self.assertEqual(t.reverse_preorder(), expected)
        self.assertEqual(t.reverse_postorder(), expected)
        self.assertEqual(t.reverse_inorder(), expected)

if __name__ == "__main__":
    unittest.main()
