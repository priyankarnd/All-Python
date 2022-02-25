# super class
class Student:

    #Protected data members
    # _name, _id, _division

    # Constructor
    def __init__(self, name, id, branch):
        self.__name = name
        self.__id = id
        self.__branch = branch

    # Protected member function
    def __displayinfo(self):
        print("Name: ", self.__name)
        print("id: ", self.__id)
        print("branch: ", self.__branch)

    # Access private data members
    def getname(self):
        return self.__name

    # Public member function
    def accessPrivateFunction(self):
        #Access private member function
        self.__displayinfo()


# Derived class
class Nerd(Student):

    # Constructor
    def __init__(self, name, id, branch):
        Student.__init__(self, name, id, branch)

    # Public member function
    def displayDetails(self):
        # Access private member function of super class through public class
        self.accessPrivateFunction()

        # Access protected data members of super class
        print("Name: ", self.getname())

n = Nerd("John", 25, "Science")

n.displayDetails()

# Access member of private class from outside directly
s = Student("Ben", 32, "Business")
print("id : ", s._Student__id)

