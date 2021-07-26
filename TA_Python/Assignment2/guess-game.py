import random

r = random.randint(1, 20) #Generate a random integer
print(f'The generated number is {r}')

attempt = 0   #attempt counter

while ( attempt < 4 ):  #Execute for 4 attempts

    print("Enter a guess number: ")
    n = input()  # Input user number
    n = int(n)
    print(f'Guessed number is: {n}')

    if (n > r):
        if (attempt < 3):
            print("Guess is high, please guess again")
        else:
            print("Guess is high, chance over")
        attempt += 1
    elif (n < r):
        if (attempt < 3):
            print("Guess is low, please guess again")
        else:
            print("Guess is high, chance over")
        attempt += 1
    else:
        attempt = 5

else :
    if (attempt != 5):
        print(f'Sorry, but the number was {r}')
    else:
        print("Congratulations, guess is correct")










