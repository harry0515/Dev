''' minimum depth of BST
    *if root is null, return o
    * if root is leaf, return 1
    * if left node of root is not null, recursively call
        getMinDepth to get left Depth
        else set leftDepth to MAX_Value
    * if right node of root is not null, recursively call
        getMindepth to get right Depth
        else set right depth to max_value
    * return 1+min of leftdepth or rightDepth'''

from TreeNode import TreeNode
from sortedArrayToBST import sortedArrayToBST

class minDepthofBST(object):
    def minDepth(self,root):
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return 1
        if root.left!=None:
            leftDepth = self.minDepth(root.left)
        else:
            leftDepth=99999

        if root.right!=None:
            rightDepth = self.minDepth(root.right)
        else:
            rightDepth = 99999
        return 1+ min(leftDepth,rightDepth)
        pass



numbs = [1, 2, 3, 4, 5, 6, 7, 8, 9]

x = sortedArrayToBST()
a = x.sortedArray(numbs)

y = minDepthofBST()

print y.minDepth(a)


