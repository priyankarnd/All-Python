#Strings

a = "Hello"
print(a)

#Multi-line strings

a = """This is a multi-line string in
Python. You can use this method 
if there is a lot of information you want to
assign to a string"""

print(a)

a = '''This is a multi-line string in
Python. You can use this method 
if there is a lot of information you want to
assign to a string'''

print(a)

#Strings are arrays
a = "Hello, World!"
print(a[0])
print(a[1])

#Slicing
b = "Hello, World!"
print(b[2:5])

#Negative Indexing
b = "Hello, World!"
print(b[-5:-2])

#String length
b = "Hello, World!"
print(len(b))

#string methods

#strip() - remove whitespaces
a = " Hello, World! "
print(a.strip())



#check if character(s) are present
txt = "The rain in Spain mainly stays in the plain"
x = "ain" in txt

print(x)

#find

txt = "It is a great day to code python"
print(txt.find("great"))   #returns lowest index of first occurence of search string

#isnumeric
txt = "1250"
print(txt.isnumeric())

#convert to uppercase
txt = "Hello World"
print(txt.upper())

#String concatenation
a = "Hello"
b = "World"

c = a + b
print(c)

#format
age= 25
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars"
print(myorder.format(quantity,itemno,price))


quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}"
print(myorder.format(quantity,itemno,price))


#formatting operator
print("Hello %s, you scored %i out of %i" % ("John", 95, 100 ))

#split into list
sentence = "There has never been a better time to learn Python"
words = sentence.split()
print(words)

# replace
b = "Honda CRV"
print(b.replace("CRV","Passport"))


#Reverse the list
words.reverse()
print(" ".join(words))

print("I am a \r grad teacher")  #new string starting after, called carriage return
print("I am a \t grad teacher")  #t represents tab
print("I am a \n grad teacher")  #n represents new line

print("""\
      Hello:
        User defined look
                """)

# Title format
a = "I own a Honda suv"
print(a.title())

# Change to opposite case
a = "Toyota and Honda are competitors"
print(a.swapcase())











