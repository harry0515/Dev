
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        start = 0
        end = len(nums)-1
        return self.BST(start,end,nums)

    def BST(self,start,end,nums):
        if start>end:
            return None
        mid = (start+end)//2
        root = TreeNode(nums[mid])
        root.left=self.BST(start,mid-1,nums)
        root.right=self.BST(mid+1,end,nums)
        return root

    def printing(self,root):
        if root.left!=None:
            self.printing(root.left)
        print root.val
        if root.right!=None:
            self.printing(root.right)



nums = [1,2,3,4,5,6,7,8,9]

x = Solution()
a = x.sortedArrayToBST(nums)

x.printing(a)



