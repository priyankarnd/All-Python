#Define a class

class Country:
    a = "USA"
    b = "Canada"
    def print_country(self):
        print("US and Canada are neighbors")

c = Country()
print(c.a)
print(c.b)
c.print_country()

# Constructor
class Car:
    def __init__(self,year,maker, model):
        self.year = year
        self.maker = maker
        self.model = model

    def price_dep(self):
        print("Year: ", self.year)


# Object
c1 = Car(2017, "Toyota", "Rav4")
c2 = Car(2021, "Honda", "Accord")

# Calling public data member
print(c1.year)
print(c1.maker)
print(c2.model)

# Calling public member function
c1.price_dep()
c2.price_dep()




    


