# ## Exercise: Class and Objects

# 1. Create a sample class named Employee with two attributes id and name 


# employee :
#     id
#     name

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display(self):
        print(f"ID: {self.id}, Name: {self.name}")
    

# object initializes id and name dynamically for every Employee object created.
 

# emp = Employee(1, "coder")
employee = Employee(1, "Programmer")
employee.display()


# 2. Use del property to first delete id attribute and then the entire object

del employee.id
try:
    print(employee.id)
except AttributeError:
    print("Employee.id is not defined")

del employee
try:
    employee.display()
except NameError:
    print("Employee is not defined")
