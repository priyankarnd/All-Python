sentence = "There has never been a better time to learn Python"

length = len(sentence)

print(length)

# print(sentence[1])

a = ""
b = "b"
c = a + b
print(c)

d = c
print(d)

interm = ""
word = ""
result = ""

for i in range(length):
    if sentence[i] != " ":
        interm = interm + sentence[i]
        word = interm
        # print(word)
    else:
        result = word + " " + result
        # print(result)
        interm = ""

result = word + " " + result
print(result)










