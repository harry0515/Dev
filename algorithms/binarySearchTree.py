from TreeNode import TreeNode


class binarySearchTree(object):

    def __init__(self):
        self.root = None

    def insert(self,value):
        if self.root==None:
            self.root = TreeNode(value)
        else:
            self._insert(value,self.root)

    def _insert(self,value,currentNode):
        if value < currentNode.val:
            if currentNode.left==None:
                currentNode.left = TreeNode(value)
            else:
                self._insert(value, currentNode.left)
        if value > currentNode.val:
            if currentNode.right==None:
                currentNode.right = TreeNode(value)
            else:
                self._insert(value, currentNode.right)

    def height(self):
        if self.root!=None:
            return self._height(self.root,-1)
        else:
            return -1

    def _height(self, currentNode, currentHt):
        if currentNode==None: return currentHt
        leftHt=self._height(currentNode.left, currentHt+1)
        rightHt=self._height(currentNode.right, currentHt+1)
        return max(leftHt,rightHt)

tree = binarySearchTree()

tree.insert(30)
tree.insert(5)
tree.insert(0)
tree.insert(1)
tree.insert(9)
tree.insert(10)
tree.insert(12)
tree.insert(35)
tree.insert(45)
tree.insert(99)
tree.insert(13)

print tree.height()

