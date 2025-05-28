# ## Exercise: Raise Exception And Finally

# 1. Create a custom exception AdultException.
# class AdultException(Exception):
#     def __init__(self, age):
#         self.age = age

#     def old(self):
#         print("Person is too old")


# class IsMajor(Exception):
#     def __init__(self, age):
#         self.age = age
    
#     def young(self):
#         print("Person is too young")

class AdultException(Exception):
    pass

# 2. Create a class Person with attributes name and age in it.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # def get_minor_age(self):
    #     try:
    #         if self.age > 18:
    #             raise AdultException(self.age)
    #         else:
    #             return self.age
        
    #     except AdultException as e:
    #         e.old()
    
    # def display_person(self):
    #     try:
    #         if self.age < 18:
    #             raise IsMajor(self.age)
    #         else:
    #             print(self.name, self.age)
        
    #     except IsMajor as e:
    #         e.young()

    def get_minor_age(self):
        if self.age > 18:
            raise AdultException()
        else:
            return self.age

    
    def display_person(self):
        try:
            print("Age: ", self.get_minor_age())
        
        except AdultException: # Custom exception
            print("Person is too old")
        
        finally:  # This block of code is always executed
            print("Name:", self.name)


# 3. Create a function get_minor_age() in the class. It throws an exception if the person is adult
#  otherwise returns age.

# 4. Create a function display_person() which prints the age and name of a person.
# ```
# let us say,

# if age>18 
#     he is major
# else
#     raise exception

# create cusomException named ismajor and raise it if age<18.


person = Person("Maarij", 17)
person.display_person()

