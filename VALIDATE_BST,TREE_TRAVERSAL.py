#VALIDATE BST
class TreeNode:
   def __init__(self, data, left = None, right = None):
      self.data = data
      self.left = left
      self.right = right
def insert(temp,data):
   que = []
   que.append(temp)
   while (len(que)):
      temp = que[0]
      que.pop(0)
      if (not temp.left):
         if data is not None:
            temp.left = TreeNode(data)
         else:
            temp.left = TreeNode(0)
         break
      else:
         que.append(temp.left)
      if (not temp.right):
         if data is not None:
            temp.right = TreeNode(data)
         else:
            temp.right = TreeNode(0)
         break
      else:
         que.append(temp.right)
def make_tree(elements):
   Tree = TreeNode(elements[0])
   for element in elements[1:]:
      insert(Tree, element)
   return Tree
class Solution(object):
   def isValidBST(self, root):
      return self.solve(root,-1000000000000000000000,1000000000000000000000)
   def solve(self,root,min_val,max_val):
      if root == None or root.data == 0:
         return True
      if (root.data <= min_val or root.data >=max_val):
         return False
      return self.solve(root.left,min_val,root.data) and self.solve(root.right,root.data,max_val)
ob1 = Solution()
tree = make_tree([3,1,4,None,2,None,5])
print(ob1.isValidBST(tree))
tree = make_tree([5,1,4,None,None,3,6])
print(ob1.isValidBST(tree))








#TREE TRAVERSAL

# Python program to for tree traversals

# A class that represents an individual node in a
# Binary Tree


class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key


# A function to do inorder tree traversal
def printInorder(root):

	if root:

		# First recur on left child
		printInorder(root.left)

		# then print the data of node
		print(root.val),

		# now recur on right child
		printInorder(root.right)


# A function to do postorder tree traversal
def printPostorder(root):

	if root:

		# First recur on left child
		printPostorder(root.left)

		# the recur on right child
		printPostorder(root.right)

		# now print the data of node
		print(root.val),


# A function to do preorder tree traversal
def printPreorder(root):

	if root:

		# First print the data of node
		print(root.val),

		# Then recur on left child
		printPreorder(root.left)

		# Finally recur on right child
		printPreorder(root.right)


# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print "Preorder traversal of binary tree is"
printPreorder(root)

print "\nInorder traversal of binary tree is"
printInorder(root)

print "\nPostorder traversal of binary tree is"
printPostorder(root)

