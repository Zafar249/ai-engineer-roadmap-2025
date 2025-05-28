# Binary Search tree is a tree data structure where each node is greater than it's left child
# but smaller than it's right child
# Time Complexity: best case O(log n)
#                  worst case O(n)
# Space Complextiy: O(n)

class Binary_Search_Tree:
    def __init__(self):
        self.root = Node(-1)

    def insert(self, node):
        self.root = self.insert_helper(self.root, node)

    def insert_helper(self, root, node):
        data = node.data
        if root == -1:
            return node
        if root.data == -1: # If root is empty
            root = node # Assign node being passed to the root node
            return root
        elif root.data > data: # If root is greater than current node
            root.left = self.insert_helper(root.left, node) 
            # Assign current root to the left child of the root
        else:
            root.right = self.insert_helper(root.right, node)
            # Assign current root to the right child of the root.
        return root
    

    def display(self):
        self.display_helper(self.root)

    def display_helper(self, root):
        # In order traversal
        if root != -1: # If current root isn't empty
            # Nodes will be printed in ascending order
            self.display_helper(root.left)
            print(root.data)
            self.display_helper(root.right)

    def search(self, data):
        return self.search_helper(self.root, data)

    def search_helper(self, root, data):
        if root == -1: # tree is empty
            return False
        elif root.data == data:
            return True
        elif root.data > data:
            return self.search_helper(root.left, data)
        else:
            return self.search_helper(root.right, data)

    def remove(self, data):
        if self.search(data): # If data exists in the tree
            self.remove_helper(self.root, data)
        else:
            print(data, "could not be found.")

    def remove_helper(self, root, data):
        
        if root == -1:
            return root
        elif root.data > data: # The data we want to remove is less than the root
            root.left = self.remove_helper(root.left, data)
        elif root.data < data:
            root.right = self.remove_helper(root.right, data)
        else: # Node found
            if (root.left == -1 and root.right == -1):
                return -1
            elif root.left == -1: # Only right child exists
                return root.right
            elif root.right == -1: # Only left child exists
                return root.left
            elif root.right != -1: # Find a successor to replace the right child
                root.data = self.successor(root)
                root.right = self.remove_helper(root.right, root.data)
            else: # Find a predecessor to replace the left child
                root.data = self.predecessor(root)
                root.left = self.remove_helper(root.left, root.data)

        return root

    def successor(self, root): # Find least value below the right child of this root node
        root = root.right
        while root.left != -1:
            root = root.left
        return root.data

    def predecessor(self, root): # Find greatest value below the left child of this root node
        root = root.left
        while root.right != -1:
            root = root.right
        return root.data

class Node:
    def __init__(self, data):
        self.data = data
        self.left = -1
        self.right = -1


tree = Binary_Search_Tree()
tree.insert(Node(5))
tree.insert(Node(2))
tree.insert(Node(7))
tree.insert(Node(6))
tree.insert(Node(3))
tree.insert(Node(1))
tree.remove(2)
tree.display()
