from collections import deque
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def construct_tree(level_order_values):
    if not level_order_values:
        return None

    # Initialize the root of the tree
    root = TreeNode(level_order_values[0])
    queue = deque([root])

    index = 1
    while queue and index < len(level_order_values):
        current_node = queue.popleft()

        # Add the left child if present
        if level_order_values[index] is not None:
            current_node.left = TreeNode(level_order_values[index])
            queue.append(current_node.left)
        index += 1

        # Ensure we have not run out of nodes to add
        if index >= len(level_order_values):
            break

        # Add the right child if present
        if level_order_values[index] is not None:
            current_node.right = TreeNode(level_order_values[index])
            queue.append(current_node.right)
        index += 1

    return root

