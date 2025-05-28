# Tree traversal is the process of visiting all the nodes in a tree
# There are three kinds of tree traversal: pre-order, in-order, post-order
# In in-order we go from left node to root node to right node
# In post-order we go from left node to right node to root node. 
# Used to delete a tree from leaf to root. Also used in RPN expressions.
# In pre-order we go from root node to left node to right node. Used to create a copy of a tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = -1
        self.right = -1
        
def inorder_traversal(self, root):
    # In order traversal
    if root != -1: # If current root isn't empty
        # Nodes will be printed in ascending order
        self.inorder_traversal(root.left)
        print(root.data)
        self.inorder_traversal(root.right)

def postorder_traversal(self, root):
    # In order traversal
    if root != -1: # If current root isn't empty
        # Nodes will be printed in ascending order
        self.postorder_traversal(root.left)
        self.postorder_traversal(root.right)
        print(root.data)

def preorder_traversal(self, root):
    # In order traversal
    if root != -1: # If current root isn't empty
        # Nodes will be printed in ascending order
        print(root.data)
        self.preorder_traversal(root.left)
        self.preorder_traversal(root.right)
