class TreeNode:
    def __init__(self, name, designation):
        self.data = [name, designation]
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, choice):
        if choice == "both":
            value = self.data[0]+ " ("+self.data[1]+")"
        elif choice == "name":
            value = self.data[0]
        elif choice == "designation":
            value = self.data[1]

        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + value)   
        if self.children:
            for child in self.children:
                child.print_tree(choice)


    def add_child(self, child):
        child.parent = self
        self.children.append(child)

# def build_product_tree():
#     root = TreeNode("Electronics")

#     laptop = TreeNode("Laptop")
#     laptop.add_child(TreeNode("Mac"))
#     laptop.add_child(TreeNode("Surface"))
#     laptop.add_child(TreeNode("Thinkpad"))

#     cellphone = TreeNode("Cell Phone")
#     cellphone.add_child(TreeNode("iPhone"))
#     cellphone.add_child(TreeNode("Google Pixel"))
#     cellphone.add_child(TreeNode("Vivo"))

#     tv = TreeNode("TV")
#     tv.add_child(TreeNode("Samsung"))
#     tv.add_child(TreeNode("LG"))

#     root.add_child(laptop)
#     root.add_child(cellphone)
#     root.add_child(tv)

#     root.print_tree()

# if __name__ == '__main__':
#     build_product_tree()

# 1. Below is the management hierarchy of a company.

# Extent [tree class] built in our main tutorial so that
# it takes **name** and **designation** in data part of TreeNode class.
# Now extend print_tree function such that it can print either name tree, 
# designation tree or name and designation tree. As shown below,

# Here is how your main function should will look like,

def build_management_tree():
    root = TreeNode("Nilpul", "CEO")

    cto = TreeNode("Chinway", "CTO")


    infrastructure = TreeNode("Vishwa", "Infrastructure Head")
    infrastructure.add_child(TreeNode("Dhaval", "Cloud Manager"))
    infrastructure.add_child(TreeNode("Abhijit", "App Manager"))

    cto.add_child(infrastructure)
    cto.add_child(TreeNode("Aamir", "Application Head"))

    hr = TreeNode("Gels", "HR Head")
    hr.add_child(TreeNode("Peter", "Recruitment Manager"))
    hr.add_child(TreeNode("Waqas", "Policy Manager"))

    root.add_child(cto)
    root.add_child(hr)

    return root

root_node = build_management_tree()
root_node.print_tree("name") # prints only name hierarchy
root_node.print_tree("designation") # prints only designation hierarchy
root_node.print_tree("both") # prints both (name and designation) hierarchy

# 2. Build below location tree using **TreeNode** class

# def build_location_tree():
#     root = TreeNode("Global")

#     pakistan = TreeNode("Pakistan")
    
#     punjab = TreeNode("Punjab")
#     punjab.add_child(TreeNode("Lahore"))
#     punjab.add_child(TreeNode("Bahawalpur"))

#     sindh = TreeNode("Sindh")
#     sindh.add_child(TreeNode("Karachi"))
#     sindh.add_child(TreeNode("Hyderabad"))

#     usa = TreeNode("USA")
    
#     new_jersey = TreeNode("New Jersey")
#     new_jersey.add_child(TreeNode("Princeton"))
#     new_jersey.add_child(TreeNode("Trenton"))

#     california = TreeNode("California")
#     california.add_child(TreeNode("San Franciso"))
#     california.add_child(TreeNode("Mountain View"))
#     california.add_child(TreeNode("Palo Alto"))

#     pakistan.add_child(punjab)
#     pakistan.add_child(sindh)

#     usa.add_child(new_jersey)
#     usa.add_child(california)

#     root.add_child(usa)
#     root.add_child(pakistan)

#     root.print_tree(4)
# # Now modify print_tree method to take tree level as input. 
# # And that should print tree only upto that level as shown below,

# build_location_tree()

