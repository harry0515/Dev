''' Finding a lowest common ancestor of a binary tree giving two nodes A,B
    * Traverse the tree in bottom up approach
    * if node (A or B) id found, return it to its parent.
    * parent will check if it was able to get nodes from both of its child.
    * if yes, then parent is LCA
    * if no, parent will return Null if none of its child returned A or B else will return not null node.'''

from TreeNode import TreeNode
from sortedArrayToBST import sortedArrayToBST


class LowestCommonAncestor(object):
    def LCA(self,Tree,A,B):
        if Tree==None:
            return
        if Tree.val==A or Tree.val==B:
            return Tree.val
        left = self.LCA(Tree.left,A,B)
        right = self.LCA(Tree.right,A,B)
        if left!=None and right!=None:
            return Tree.val
        if left==None:
            return right
        else:
            return left


# numbs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# x = sortedArrayToBST()
# a = x.sortedArray(numbs)
#
# y = LowestCommonAncestor()
# b= y.LCA(a,1,4)
# print b