# Question 5: Text Analysis (20 Points)
# I worked with Maggie Murdok and Kelly Mitchell on this problem

# first establish the text
text = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only."

# I need to first figure out how many words are total in the paragraph

# remove punctuation
text = text.replace(",", "")
text = text.replace("–", "")
text = text.replace("!", "")
text = text.replace("?", "")
text = text.replace(".", "")

# put word in a list
text = text.split()

# count the words in the paragraph
print("There are", len(text), "words in this paragraph.")

# figure out how many different words are in this pargraph
# use a set here

uniqueset = set(text)
duplicateset = set(text)

for word in text:
    if word in uniqueset:
        duplicateset.add(word)
    else:
        uniqueset.add(word)

print("There are", len(uniqueset), "unique words in this pargaraph.")

# Make an empty dictionary to count the words and letters

WordC = {}
LetterC = {}

for word in text:
    # make everything lowercase
    word = word.lower()
    if word not in WordC:
        WordC[word] = 1  # this would be the first time the word is found
    else:
        WordC[word] += 1  # counting on top of the first word

HighestWord = text[0].lower()

# establish the highest word
for word in WordC:
    if WordC[word] > WordC[HighestWord]:
        HighestWord = word

print("The word ", "'", HighestWord, "'", "has the most occurrences,", "appearing", WordC[HighestWord], "times.")

# Use a dictionary to count the number of occurrences of each letter, and print out to the user any non-vowel letters that are used more than 25 times.

for word in text:
    for letter in word:
        letter = letter.lower()
        if letter in LetterC:
            # increase the count
            LetterC[letter] += 1
        else:  # first time it is found
            LetterC[letter] = 1

HighestLetter = []

for letter in LetterC:
    if letter in LetterC and LetterC[
        letter] > 25 and letter != "a" and letter != "e" and letter != "i" and letter != "o" and letter != "u":
        HighestLetter.append(letter)
print("These are the consonants that appear more than 25 times in the text: " + str(HighestLetter))