# ## Exercise: Multiple Inheritance

# Real Life Example :
# 1. Create multiple inheritance on teacher,student and youtuber.

# class Teacher:
#     def teach(self):
#         print("I'm teaching")

# class Student:
#     def study(self):
#         print("I'm studying.")

# class Youtuber:
#     def record(self):
#         print("I'm recording a video.")

# class Person(Teacher, Student, Youtuber):
#     def action(self):
#         Teacher.teach(self)
#         Student.study(self)
#         Youtuber.record(self)

# person = Person()
# person.action()

# Q. if we have created teacher and now one student joins master degree with becoming teacher then what??

# Ans :  just make subclass from  teacher so that student will become teacher


# 2. Now student is teacher as well as youtuber then what???

class Student:
    def study(self):
        print("I'm studying.")

class Teacher(Student):
    def teach(self):
        print("I'm teaching")


class Youtuber(Student):
    def record(self):
        print("I'm recording a video.")

class Person(Teacher, Youtuber):
    def action(self):
        Teacher.teach(self)
        Student.study(self)
        Youtuber.record(self)

person = Person()
person.action()


# -just use multiple inheritance for these three relations


