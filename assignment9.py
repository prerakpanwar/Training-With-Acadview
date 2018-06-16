#Q1- Create a class Animal as a base class and define method animal_attribute.

print("Create another class Tiger which is inheriting Animal and access the base class method.\n")


class Animal:

    def animal_attribute(self):
        print("Base class is inherited")

class Tiger(Animal):

    def __init__(self):
        self.animal_attribute()

obj = Tiger()





#Q2- What will be the output of following code.

# Output  : A B
#      	    A B






#Q3- Create a class Cop. Initialize its name, age , work experience and designation.

print("Define methods to add, display and update the following details.")
print("Create another class Mission which extends the class Cop.")
print("Define method add_mission _details.")
print("Select an object of Cop and access methods of base class to get information for a particular cop and make it available for mission.\n")


class Cop:

    def __init__(self, name, age, work_experience, designation):
        self.name = name
        self.age = age
        self.work_experience = work_experience
        self.designation = designation

    def add(self):
        print("\nADD....")
        self.name = input("Enter name            : ")
        self.age = input("Enter age             : ")
        self.work_experience = input("Enter work experience : ")
        self.designation = input("Enter designation     : ")

    def display(self):
        print("\nDISPLAY....")
        print("Name of cop            : " + str(self.name))
        print("Age of cop             : " + str(self.age))
        print("Work experience of cop : " + str(self.work_experience))
        print("Designation of cop     : " + str(self.designation))

    def update(self):
        print("\nUPDATE....")
        self.name = input("Enter name            : ")
        self.age = input("Enter age             : ")
        self.work_experience = input("Enter work experience : ")
        self.designation = input("Enter designation     : ")


class Mission(Cop):
    def add_mission_details(self):
        print("\nCOP IS READY FOR MISSION.......")

c = Cop('name', 'age', 'work experience', 'designation')
c.add()
c.display()
c.update()
c.display()






#Q4- Create a class Shape.

print("Initialize it with length and breadth Create the method Area.")
print("Create class rectangle and square which inherits shape and access the method Area.\n")


class Shape:
    def __init__(self, length , breath):
        self.length = length
        self.breath = breath

    def Area(self):

        print("Area is : " + str(self.length * self.breath))



class Rectangle(Shape):

    def __init__(self, length, breath):
        self.length = length
        self.breath = breath


class Square(Shape):

    def __init__(self, length, breath):
        self.length = length
        self.breath = breath

A = Rectangle(int(input("Enter length of rectangle : ")), int(input("Enter breath of rectangle : ")))
A.Area()

B = Square(int(input("Enter side of square : ")), int(input("Enter breath of square : ")))
B.Area()
