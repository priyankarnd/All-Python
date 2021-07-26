names = ['Liam', 'Noah', 'Oliver', 'William', 'Elijah', 'James', 'Benjamin', 'Lucas', 'Mason', 'Ethan']  #popular names

#Initialize indices
#a = 0
# b = 1
# c = 2

count = 1 #line no.

for a in range(0,8):
    b = a + 1
    c = a + 2
    for c in range(c,10):
        print(f'{a} {b} {c}')
        print(f'{count}: {names[a]}, {names[b]}, {names[c]}')
        count += 1
    # b += 1
    # c += 1

