# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root,k):
        l = []
        self.result = 0
        self.k = k

        def inorder(root):
            if (root):
                inorder(root.left)
                self.k -= 1
                if (self.k == 0):
                    self.result = root.val
                    return
                inorder(root.right)

        inorder(root)
        return self.result

treenode = TreeNode(1)
treenode.left = TreeNode(4)
treenode.right = TreeNode(9)
treenode.left.left = TreeNode(3)
treenode.left.right = TreeNode(5)

soln = Solution()
soln.kthSmallest(treenode,2)
