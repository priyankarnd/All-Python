input = "The weather is great today"

# a,e,i,o,u = 0,0,0,0,0

# for x in input:
#     if (x == 'a'):
#         a = a + 1
#     elif (x == 'e'):
#         e = e + 1
#     elif (x == 'i'):
#         i = i + 1
#     elif (x == 'o'):
#         o = o + 1
#     elif (x == 'u'):
#         u = u + 1

# print("a - " + str(a) + " times")
# print("e - " + str(e) + " times")
# print("i - " + str(i) + " times")
# print("o - " + str(o) + " times")
# print("u - " + str(u) + " times")

#Posted solution

vowels = { }

for x in input:
    if x in ["a", "e", "i", "o", "u"]:
        if x in vowels:
            vowels[x] += 1
        else:
            vowels[x] = 1

print(vowels)

#My solution

vowels = { }

for i in input:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        if i in vowels:
            vowels[i] += 1
        else:
            vowels[i] = 1

print(vowels)

#print sorted results
for index in sorted(vowels):
    print(index, ":", vowels[index])








