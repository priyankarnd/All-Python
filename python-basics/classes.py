#Defining a class

class MyClass:
    a = 10
    b = 20

x = MyClass()
print(x.a)
print(x.b)

class Person :
    #1. constructor
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    #2. Methods
    def fullName(self):
        return f'{self.firstName} {self.lastName}'

#3. Inheritance

class Customer (Person) :
    gender = "male"
    def __init__(self, id, firstName, lastName, age):
        super().__init__(firstName, lastName, age)
        self._id = id  #Private property of child class

    def getBalance(self):
        return 10

    def getCustomerId (self):  #Method to access private property
        return str(self._id)


class Employee (Person):
    def __init__(self, id, firstName, lastName, age):
        super().__init__(firstName, lastName, age)
        # Private variable
        self.__id = id

    def getDepartment(self):
        #retrieve from database
        return "Sales"

    def getYearsofService(self):
        return 5

    def getEmployeeID(self):
        return str(self.__id)


#Creating a Person Object
p = Person("Mike", "Smith", 35)

print(p.firstName)
print(p.age)
print(p.fullName())

# Passing new value
p.firstName = "Jack"
print(p.firstName)

# Deleting object
del p

#Creating a customer object
c = Customer (34, "Mary", "Smith", 40)
print(c.gender)

#Inherited Method
print(c.fullName())

print(c.getBalance())

#accessing private variables
c = Customer (34, "Mary", "Smith", 40)

print(c._id) #No protection; still accessible
print(c.getCustomerId())

e = Employee(50, "Harold", "Thompson", 55)

#print(e.__id) # protected, will now work

print(e.getEmployeeID())

print(e._Employee__id) #Behind the scenes, how Python accesses

print(e.getYearsofService())

print(e.getDepartment())




