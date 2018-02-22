'''sorted arrray to binary search tree

    * intialize start=0, end= length of array -1
    * mid = start+end//2
    * create a tree node with mid as root.
    * recursively calculate mid of left subarray and make it root of left subtree of A
    * recursivley calculate mid of right subarray and make it root of right subtree of A
    * return root'''

from TreeNode import TreeNode


class sortedArrayToBST(object):
    def sortedArray(self, nums):
        start = 0
        end = len(nums) - 1
        return self.BST(start, end, nums)

    def BST(self, start, end, nums):
        if start > end:
            return None
        mid = (start + end) // 2
        root = TreeNode(nums[mid])
        root.left = self.BST(start, mid - 1, nums)
        root.right = self.BST(mid + 1, end, nums)
        return root

    def printing(self, root):
        if root is None:
            return
        if root.left != None:
            self.printing(root.left)
        print root.val
        if root.right != None:
            self.printing(root.right)

#
# numbs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# x = sortedArrayToBST()
# a = x.sortedArray(numbs)
# print x.printing(a)
