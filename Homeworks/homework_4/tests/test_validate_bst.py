import unittest
from validate_bst.src.validate_bst import *


class TestIsBST(unittest.TestCase):
    # пустое дерево
    def test_empty_tree(self):
        self.assertTrue(is_bst(None))

    # один узел
    def test_single_node(self):
        self.assertTrue(is_bst(Node(10)))

    # корректный маленький BST
    def test_small_valid_bst(self):
        root = Node(2, Node(1), Node(3))
        self.assertTrue(is_bst(root))

    # нарушение: левый потомок больше родителя
    def test_direct_violation_left_child(self):
        root = Node(2, Node(5), Node(3))
        self.assertFalse(is_bst(root))

    # нарушение: правый потомок меньше родителя
    def test_direct_violation_right_child(self):
        root = Node(2, Node(1), Node(0))
        self.assertFalse(is_bst(root))

    # глубокое нарушение в левом поддереве
    def test_deep_violation_left_subtree(self):
        root = Node(10,
                    Node(5, Node(2), Node(12)),
                    Node(15))
        self.assertFalse(is_bst(root))

    # глубокое нарушение в правом поддереве
    def test_deep_violation_right_subtree(self):
        root = Node(10,
                    Node(5),
                    Node(15, Node(6), Node(20)))
        self.assertFalse(is_bst(root))

    # дубликат в левом поддереве
    def test_duplicate_left(self):
        root = Node(5, Node(5), Node(7))
        self.assertFalse(is_bst(root))

    # дубликат в правом поддереве
    def test_duplicate_right(self):
        root = Node(5, Node(3), Node(5))
        self.assertFalse(is_bst(root))

    # сильно перекошенное дерево влево
    def test_skewed_left(self):
        root = Node(5,
                    Node(4,
                         Node(3,
                              Node(2,
                                   Node(1)))))
        self.assertTrue(is_bst(root))

    # сильно перекошенное дерево вправо
    def test_skewed_right(self):
        root = Node(1,
                    None,
                    Node(2,
                         None,
                         Node(3,
                              None,
                              Node(4,
                                   None,
                                   Node(5)))))
        self.assertTrue(is_bst(root))


if __name__ == "__main__":
    unittest.main()
