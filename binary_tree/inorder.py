class Node:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.val = val
        self.right = right

def inorderTraversal(root):
    if root:
        left = inorderTraversal(root.left)
        val = root.val
        right = inorderTraversal(root.right)
        return (left + [val] + right)
    else:
        return []

def non_rec(root):
    res = []  #adding the root.val
    stack = [] #keeping track of current nodes.
    current = root  #for simplicity and naming

    while current or stack:  #while stakc is not empty or current stack. outer loop
        while current:  #getting the left-most subtree.
            stack.append(current) #add the current node to stack.
            current = current.left #go to left most node.

        current = stack.pop()  #once current meet the left most node, pop from stack
        res.append(current.val)  #add it's value to stack

        current = current.right  #go to rigth node.

    return res


def preOrder(root):
    if not root:
        return []

    stack = [root]
    res = []

    while stack:
        node = stack.pop()
        res.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return res
root = Node(3)
root.left = Node(4)
root.left.right = Node(5)
root.left.left = Node(5)


print(non_rec(root))
print(preOrder(root))
