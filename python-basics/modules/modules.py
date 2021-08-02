import greeting
import greeting as gt #alias
from greeting import name_greeting #import a function
from greeting import fullname_greeting as full_greet


#executing a function from the module
greeting.name_greeting("Smith")

#accessing a variable from the module
greeting.person = "John"
greeting.morning_greeting()

#using an alias
gt.morning_greeting()

#import specific function from the module
name_greeting("Jason")

#import specific function with an alias
full_greet("Mary", "Smith")

#show a list of special variables
print(dir())


if __name__ == "__main__":
    print("modules.py is being run")
    name_greeting("from main of modules.py")

print(gt.message_list)
print(gt.message_list[1])

from os_name import xt

print(xt)



