x = 50

txt = "The price is {} USD"

print(txt.format(x))

txt = "The price is {:.2f} USD"  # up to two decimal places
print(txt.format(x))

a = 50
b = 44
c = 72

txt = "I want {} pieces of item number {} for {:.2f} USD each"

print(txt.format(a,b,c))
print(txt.format(b,c,a))
print(txt.format(c,a,b))


txt = "I want {0} pieces of item number {1} for {2:.2f} USD each"
print(txt.format(a,b,c))

txt = "I want {1} pieces of item number {2} for {0:.2f} USD each"
print(txt.format(a,b,c))

txt = "I want {2} pieces of item number {1} for {0:.2f} USD each"
print(txt.format(a,b,c))

age = 29
name = "Prix"

txt = "My name is {1}. {1} is {0} years old."

print(txt.format(age, name))

txt = "I have a {car_manufacturer}. The model is {model}"
print(txt.format(car_manufacturer = "Honda", model="CRV"))






