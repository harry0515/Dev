'''finding max depth of a binary search  tree'''

from TreeNode import TreeNode
from sortedArrayToBST import sortedArrayToBST

class maxDepthofBST(object):
    def maxDepth(self,root):
        if root == None:
            return 0
        if root.left==None and root.right==None:
            return 1
        if root.left!=None:
            leftDepth = self.maxDepth(root.left)
        else:
            leftDepth = -1
        if root.right!=None:
            rightDepth = self.maxDepth(root.right)
        else:
            rightDepth = -1
        return 1+ max(leftDepth,rightDepth)



numbs = [1, 2, 3, 4, 5, 6, 7, 8, 9]

x = sortedArrayToBST()
a = x.sortedArray(numbs)

y = maxDepthofBST()

print y.maxDepth(a)
