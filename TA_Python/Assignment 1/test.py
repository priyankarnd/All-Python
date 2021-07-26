import random
new_word = input("Word:")
if (len(new_word) < 5): # If the length of the word is <5 letters, this prints the word
    print(new_word)
if (len(new_word) >= 5 and len(new_word) <= 8): # This generates a random integer between 1 and 10 if the word has 5-8 letters
    randinteger = random.randint(1,10)
    if (randinteger % 2 == 0): # This prints the word in capital letters if the random integer is even
        print(new_word.upper())
    else: # This prints Go Irish! if random integer is odd
        print("Go Irish!")
if ((len(new_word) > 8) and (("r" or "R") in new_word)): # This prints a statement if the word has r or R
    print("This long word has the letter R")
if ((len(new_word) > 8) and (("r" or "R") not in new_word)): # This prints a statement if the word does not have r or R
    print("This long word does not have the letter R")