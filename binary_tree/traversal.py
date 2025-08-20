class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

"""there are two ways to traverse throught he BST without recurssion"""

#without True
def non_rec_bst(root, item):
    newNode = Node(item)
    if root is None:
        root = newNode
        return True

    current = root 
    while True:
        if item < current.value:
            if current.left is None:
                current.left = newNode
                return True
            current = current.left
        elif item > current.value:
            if current.right is None:
                current.right = newNode
                return True
            current = current.right
        else:
            return False 


def non_rec_bst_two(root, item):
    newNode = Node(item)
    if root is None:
        root = newNode
        return root

    current = root
    parent = None

    while current:
        parent = current 
        if item < current.value:
            current = current.left
        elif item > current.value:
            current = current.right
        else:
            return root

    if item < parent.value:
        parent.left = newNode
    elif item > parent.value: 
        parent.right = newNode

    return root


def rec_bst(root, item):
    if root is None:
        return Node(item) 

    if item < root.value:
        root.left = rec_bst(root.left, item)
    else:
        root.right = rec_bst(root.right, item)

    return root


root = Node(1)
rec_bst(root, 2)
rec_bst(root, 3)
rec_bst(root, 4)
rec_bst(root, 5)

#inorder traversal over the tree.
def inOrder(root):  #LNR
    if root:   #checking is it null or what.
        inOrder(root.left)
        print(f"{root.value} ->", end=" ")
        inOrder(root.right)

def preOrder(root):  #NLR
    if root:
        print(f"{root.value} -> ")
        preOrder(root.left)
        preOrder(root.right)

def postOrder(root): #LRN
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(f"{root.value} -> ")


inOrder(root)

