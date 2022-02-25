import re 
#regular expression

text = "This is Book"
x = re.search("^This.*Book$",text) # First and last word

if x:
    print("Yes, match found")
else:
    print("No, match not found")

txt = "The rain in India and Indian rain"
x = re.findall("ai", txt)   # Occurrences

print(x)

x = re.search("\s", txt)  # search for the position
print(f'The first whitespace is located at position {x.start()}')

x = re.search("post", txt)  
print(x)

x = re.split("\s", txt, 1)  #  split at particular positions
print(x)

x = re.split("\s", txt, 2)
print(x)

x = re.split("\s", txt, 3)
print(x)

x = re.sub("\s","-", txt)
print(x)











