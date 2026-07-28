class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.depth = 1

    def insertNode(self, root,  val):
        if root is None:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insertNode(root.left, val)
        else:
            root.right = self.insertNode(root.right, val)

        return root

    def search(self, root, target):
        if root is None: return False

        if root.val == target:
            return True


        if target < root.val:
            return self.search(root.left, target)

        return self.search(root.right, target)

    def delete(self, root, val):
        if root is None: return None

        if val < root.val:
            root.left = self.delete(root.left, val)
        elif val > root.val:
            root.right = self.delete(root.right, val)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            temp = root.right
            while temp.left:
                curr = temp.left

            root = temp.val
            return self.delete(root.right, temp.val)

        return root


    def search_itr(self, root, target):
        while root:
            if target == root.val:
                return True
            elif target < root.val:
                root = root.left
            else:
                root = root.right

        return False

    def itr_pre(self):
        if self.root is None: return
        stack = [self.root]
        while stack:
            curr = stack.pop()
            print(curr.val, end=" ")
            if curr.right: stack.append(curr.right)
            if curr.left: stack.append(curr.left)

        return

    def preorder(self, root):
        if not root: return
        
        print(root.val, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    def itr_inr(self):
        if not self.root: return
        stack = []
        curr = self.root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            print(curr.val, end=" ")
            
            curr = curr.right

        return

    def itr_post(self):
        if not self.root: return
        stack1 = []
        stack2 = []
        curr = self.root
        while curr:
            stack1.append(self.root.right)
            curr = curr.right
            if curr.left: stack1.append(curr.left)
        return

    def inorder(self, root):
        if not root: return

        self.inorder(root.left)
        print(root.val, end=" ")
        self.inorder(root.right)

    def postorder(self, root):
        if not root: return

        self.postorder(root.left)
        self.postorder(root.right)
        print(root.val, end=" ")

    def lvl_travers(self, root):
        from collections import deque

        q = deque()
        q.append(root)
        q.append(None)

        while q:
            curr = q.popleft()

            if curr==None and len(q) != 0:
                self.depth += 1
                q.append(None)
            
            if curr != None: 
                print(curr.val, end=" ")
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)



bst = BST()
nums = [10, 5, 15, 3, 8, 12, 20]

for x in nums:
    bst.root = bst.insertNode(bst.root, x)


yoo = bst.search_itr(bst.root, 21)
bst.lvl_travers(bst.root)
print(yoo)
print(yoo)
bst.preorder(bst.root)
print(yoo, "preorder")
bst.inorder(bst.root)
print(yoo, "inorder")
bst.postorder(bst.root)
print(yoo, "postorder")

print(bst.depth)

bst.delete(bst.root, 8)
print()
print(yoo, "postorder")
# sarch in BST:

print("fuck it")
bst.itr_inr()
