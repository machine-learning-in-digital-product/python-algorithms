import unittest
from traversal.src.node import *
from balanced_binary_tree.src.balanced_binary_tree import *


class TestIsBalanced(unittest.TestCase):
    # 1. Пустое дерево
    def test_empty_tree(self):
        self.assertTrue(is_balanced(None))

    # 2. Один узел
    def test_single_node(self):
        self.assertTrue(is_balanced(Node(1)))

    # 3. Дерево из двух уровней, один ребёнок
    def test_root_with_one_child(self):
        root = Node(1, Node(2))   # разница высот = 1
        self.assertTrue(is_balanced(root))

    # 4. Идеально сбалансированное дерево
    def test_perfect_tree(self):
        root = Node(2, Node(1), Node(3))
        self.assertTrue(is_balanced(root))

    # 5. Сбалансированное, но не идеальное дерево
    def test_balanced_not_perfect(self):
        root = Node(2,
                    Node(1),
                    Node(3, None, Node(4)))
        self.assertTrue(is_balanced(root))

    # 6. Несбалансированное дерево — перекос у корня
    def test_unbalanced_root(self):
        root = Node(1,
                    Node(2,
                         Node(3)))
        self.assertFalse(is_balanced(root))

    # 7. Несбалансированное дерево — перекос глубже
    def test_unbalanced_deep(self):
        root = Node(4,
                    Node(2,
                         Node(1,
                              Node(0)),
                         None),
                    Node(6, Node(5), None))
        self.assertFalse(is_balanced(root))

    # 8. Сильно перекошенное влево дерево
    def test_skewed_left(self):
        root = Node(5,
                    Node(4,
                         Node(3,
                              Node(2,
                                   Node(1)))))
        self.assertFalse(is_balanced(root))

    # 9. Сильно перекошенное вправо дерево
    def test_skewed_right(self):
        root = Node(1,
                    None,
                    Node(2,
                         None,
                         Node(3,
                              None,
                              Node(4))))
        self.assertFalse(is_balanced(root))

    # 10. Большое сбалансированное дерево
    def test_large_balanced(self):
        root = Node(4,
                    Node(2, Node(1), Node(3)),
                    Node(6, Node(5), Node(7)))
        self.assertTrue(is_balanced(root))


if __name__ == "__main__":
    unittest.main()
