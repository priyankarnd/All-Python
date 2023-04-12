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

class usa:
    def __init__(self, continent,capital):
        self._continent = continent
        self._capital = capital
        
    def _print_capital(self):
        print("Capital is: ", self._capital)

class state(usa):
    def __init__(self, continent, capital,region,timezone):
        usa.__init__(self, continent, capital)
        self.region = region
        self.timezone = timezone

    def print_continent(self):
        print(self._continent)
    
    def print_capital(self):
        self._print_capital()

s = state("North America", "Washington D.C","Rockies","MST")
s.print_continent()
print(s.region)
s.print_capital()

