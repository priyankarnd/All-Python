def sum (*numbers):
    result = []
    for x in numbers:
        result.append(x)
    result.sort(reverse = True)
    print(result)

sum(1,6,3,12,29,17,34)
sum(1,6,3,12,29,17,12)

# txt = "Hello"
# for x in txt:
#     print(x)

def case_char_count (input):
    upper = 0
    lower = 0
    # print(input)
    for x in input:
        # print(x)
        if x.isupper() :
            upper += 1
        elif x.islower():
            lower += 1
    print("No of uppercase characters: ", upper)
    print("No of lowercase characters: ", lower)

case_char_count("The weather on Monday in Atlanta is rainy")



