par = 'Every couple of months Crowley would pick out a plant that was growing too slowly, or succumbing to leaf-wilt or browning, or just did not look quite as good as the others, and he would carry it around to all the other plants. "Say goodbye to your friend," he would say to them. "He just could not cut it... " Then he would leave the flat with the offending plant, and return an hour or so later with a large, empty flower pot, which he would leave somewhere conspicuously around the flat. The plants were the most luxurious, verdant, and beautiful in London. Also the most terrified.'

par = par.replace(","," ")
par = par.replace("\""," ")
par = par.replace(".", " ")

print(par)

words = par.split()  #separate the words

print(words)  #print out words in a list format

count5 = 0   #count the no. of words with more than 5 letters

for x in words:  #Traverse the list
    if len(x) > 5:   #If more than 5 letters
        count5 += 1   #Increment

print(f'The no. of words with more than 5 letters is {count5}')

countp = 0  #count no. of words with p or P

for x in words:  #Traverse and look for p or P
    if "p" or "P" in x:
        countp += 1

print(f'The no. of words with p or P in them is: {countp}')

longest = words[0]  # save first word

print(longest)

for x in words:
    if len(x) > len(longest):   # if the word is greater than the current longest word
        longest = x

print(f'The longest word is: {longest}')













