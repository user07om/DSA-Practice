class Node:
    def __init__(self, root):
        self.left = None
        self.right = None
        self.key = root


    """
    there are three types of traversal ---
    1. inorder -> left, root, right
    2. preorder -> root, left, right
    3. postorder -> left, right, root
    """

def traverse_inOrder(root):
    if root:
        traverse_inOrder(root.left)
        print(f"{root.key} -> ", end=" ")
        traverse_inOrder(root.right)

def traverse_preOrder(root):
    if root:
        print(f"{root.key} -> ", end=" ")
        traverse_preOrder(root.left)
        traverse_preOrder(root.right)

def traverse_postOrder(root):
    if root:
        traverse_postOrder(root.left)
        traverse_postOrder(root.right)
        print(f"{root.key} -> ", end=" ")


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


# traverse_inOrder
traverse_inOrder(root)
print("inOrder")

# traverse_preOrder
traverse_preOrder(root)
print("preOrder")

# traverse_postOrder
traverse_postOrder(root)
print("postOrder")

