from traversal.src.node import Node

def is_bst(current_node, low=float('-inf'), high=float('inf')):
    if current_node is None:
        return True

    if not (low < current_node.val < high):
        return False

    return (is_bst(current_node.left, low, current_node.val) and
            is_bst(current_node.right, current_node.val, high))
