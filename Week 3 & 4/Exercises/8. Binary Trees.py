class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def find_min(self):
        min = self.data
        if self.left:
            min = self.left.find_min()
        return min
    
    def find_max(self):
        max = self.data
        if self.right:
            max = self.right.find_max()
        return max
    
    def calculate_sum(self):
        sum = 0

        if self.left:
            sum += self.left.calculate_sum()
        
        sum += self.data
        
        if self.right:
            sum += self.right.calculate_sum()

        return sum

    
    def pre_order_traversal(self):
        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.in_order_traversal()

        

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        if self.right:
            elements += self.right.in_order_traversal()

        elements.append(self.data)

        return elements
    
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            # min_val = self.right.find_min()
            # self.data = min_val
            # self.right = self.right.delete(min_val)

            
            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)


def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root


# if __name__ == '__main__':
#     countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
#     country_tree = build_tree(countries)

#     print("UK is in the list? ", country_tree.search("UK"))
#     print("Sweden is in the list? ", country_tree.search("Sweden"))

#     numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
#     print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())

numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
numbers_tree.delete(20)
print(numbers_tree.in_order_traversal())

# Add following methods to [BinarySearchTreeNode class] created in main video tutorial

#     1. find_min(): finds minimum element in entire binary tree
#     2. find_max(): finds maximum element in entire binary tree
#     3. calculate_sum(): calcualtes sum of all elements
#     4. post_order_traversal(): performs post order traversal of a binary tree
#     5. pre_order_traversal(): perofrms pre order traversal of a binary tree
