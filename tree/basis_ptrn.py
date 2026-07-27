class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        ...

    def insert(self, root, val):
        if not root: return TreeNode(val)

        if val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)

        return root

    def inorder(self, root):
        if not root: return

        self.inorder(root.left)
        print(root.val)
        self.inorder(root.right)

    def preorder(self, root):
        if not root: return 

        print(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self, root):
        if not root: return

        self.postorder(root.left)
        self.postorder(root.right)
        print(root.val)

    def search(self, root, val):
        if not root: return False

        if val == root.val: return True
        elif val < root.val:
            return self.search(root.left, val)
        return self.search(root.right, val)

    def delete(self, root, val):
        if not root: return False

        if val < root.val:
            root.left = self.delete(root.left, val)
        elif val > root.val:
            root.right = self.delete(root.right, val)
        else: #when both val and root.val are equal or similar!
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            #inorder successor
            temp = root.right
            while temp.left:
                temp = temp.left

            root = temp.val
            return self.delete(root.left, temp.val)

        return root

    def lvl_ord(self, root):
        from collections import deque
        if not root: return

        q = deque([root])

        while q:
            curr = q.popleft()

            print(curr.val)
            if curr.left: q.append(curr.left)
            if curr.right: q.append(curr.right)

    def max_depth(self, root):
        if not root: return 0

        left = self.max_depth(root.left)
        right = self.max_depth(root.right)
        return max(left, right) + 1

    


if __name__=="__main__":
    bst = BST()

    arr = [4, 2, 1, 3, 6, 5, 7]
    root = None
    for x in arr:
        root = bst.insert(root, x)

    #bst.inorder(root)
    #bst.preorder(root)
    #bst.postorder(root)
    #print(bst.search(root, 5))
    #bst.delete(root, 5)
    #bst.inorder(root)
    #bst.lvl_ord(root)
    print(bst.max_depth(root))
