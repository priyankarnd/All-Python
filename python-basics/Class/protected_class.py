# super class
class Student:

    #Protected data members
    # _name, _id, _division

    # Constructor
    def __init__(self, name, id, branch):
        self._name = name
        self._id = id
        self._branch = branch

    # Protected member function
    def _displayinfo(self):
        print("Name: ", self._name)
        print("id: ", self._id)
        print("branch: ", self._branch)

# Derived class
class Nerd(Student):

    # Constructor
    def __init__(self, name, id, branch):
        Student.__init__(self, name, id, branch)

    # Public member function
    def displayDetails(self):
        # Access protected member function of super class
        self._displayinfo()

        # Access protected data members of super class
        print("Name: ", self._name)

n = Nerd("John", 25, "Science")

n.displayDetails()


