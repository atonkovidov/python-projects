#Andre Tonkovidov
#atonkovidov@ucsc.edu
#pa3
#Program randomly selects a number between 1 and 10 and allows the user 3 chances to
#guess it correctly.

from random import randint
pick = randint(1,10)
print()
print("I'm thinking of an integer in the range 1 to 10. You have 3 guesses.")
print()

guess1 = int(input('Enter your first guess: '))
if guess1 == pick:
   print("You win!")
   exit()
elif guess1 > pick:
   print("Your guess is too high.")
else:
   print("Your guess is too low.")
print()

guess2 = int(input('Enter your second guess: '))
if guess2 == pick:
   print("You win!")
   exit()
elif guess2 > pick:
   print("Your guess is too high.")
else:
   print("Your guess is too low.")
print()

guess3 = int(input('Enter your third guess: '))
if guess3 == pick:
   print("You win!")
   exit()
elif guess3 > pick:
   print("Your guess is too high.")
else:
   print("Your guess is too low.")
print()

print("You lose. The number was", str(pick), end='.')
print()