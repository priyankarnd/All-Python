para = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only."

para = para.lower()

para =para.replace("."," ")
para = para.replace("," , " ")
para = para.replace("–", " ")

print(para)

words = para.split()   #list of strings(each word)

print(words)
length = len(words)     # no. of words in the string

print(f'There are {length} words in the string')

# print(words[1])

wordstring = ""

number = 0

for x in words:
    if x not in wordstring:
        wordstring = wordstring + " " + x
        number += 1

print(wordstring)   #Number of different words

print(f'There are {number} different words used in the paragraph')

#Creating a word dictionary
word_dict = {

}

for x in words:    #check the list of words
    if x in word_dict:      #if present in dictionary
        word_dict[x] += 1
    else:                  #if not present in dictionary
        word_dict[x] = 1

print(word_dict)

largest = 0  #largest
largest_word = ""

for x in word_dict:
    if word_dict[x] > largest:   #Current value is greater than previous value
        largest = word_dict[x]   #Value
        largest_word = x    #Key

print(f'Word \'{largest_word}\' has been used {largest} number of times')

#Creating a letter dictionary
letter_dict = {

}

for x in word_dict:
    for y in x:
        if y in letter_dict:
            letter_dict[y] += 1
        else:
            letter_dict[y] = 1

print(letter_dict)

#Dictionary for printing
letter_dict2 = {

}

vowels = "aeiou"

for z in letter_dict:
    # print(z)
    if z not in vowels:
        print(z)
        print(letter_dict[z])
        if letter_dict[z] > 25:
            print(z)











