class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value 


    """
    there are three types of traversal ---
    1. inorder -> left, root, right
    2. preorder -> root, left, right
    3. postorder -> left, right, root
    """


"""
I'm not gonna spend trying to write this in OOPS concept. letter on I'll do google 
and find how can i write the operations in class and work around it in recursive way
within the class.
"""
#OPERATIONS OVER THE BINARY TREE. (recursive way and non-recursive way)
def rec_add(tree, item):
  if tree is None:
    return Node(item)

  if item < tree.value:
    tree.left = rec_add(tree.left, item)
  else:
    tree.right = rec_add(tree.right, item)

  return tree
  

def non_rec_add(root, item):
  newNode = Node(item)
  
  #add the item to node if it is None
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



def non_rec_add_two(root, item):
  newNode = Node(item)
  if root is None:
    return newNode

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
  else:
    parent.right= newNode

  return root






#TRAVERSING ON THE BINARY TREE WAYS
def traverse_inOrder(root):
    if root:
        traverse_inOrder(root.left)
        print(f"{root.value} -> ", end=" ")
        traverse_inOrder(root.right)

def traverse_preOrder(root):
    if root:
        print(f"{root.value} -> ", end=" ")
        traverse_preOrder(root.left)
        traverse_preOrder(root.right)

def traverse_postOrder(root):
    if root:
        traverse_postOrder(root.left)
        traverse_postOrder(root.right)
        print(f"{root.value} -> ", end=" ")

#
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

non_rec_add_two(root, -1)
non_rec_add_two(root, -2)
non_rec_add_two(root, -3)

# traverse_inOrder
traverse_inOrder(root)
print("inOrder")

## traverse_preOrder
traverse_preOrder(root)
print("preOrder")

## traverse_postOrder
traverse_postOrder(root)
print("postOrder")
