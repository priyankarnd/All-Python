import random

#verbs
verbs = ['do', 'play', 'jump', 'swim', 'walk']

#nouns
nouns = ['ant', 'cat', 'dog', 'rakoon', 'bunny']

a = random.randint(0,4) #use random integer generator function

#select a verb
y = verbs[a]
print(y)

a = random.randint(0,4) #use random integer generator function

#select a noun
z = nouns[a]
print(z)

print(f'Whenever I\'m about to {y}, I ask myself, "Would an {z} do that?" And if they would, I do not do that thing.')

