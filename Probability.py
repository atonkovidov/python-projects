# Andre Tonkovidov
# atonkovidov@ucsc.edu
# pa6
# The program asks the user to input the number of dice to roll, the number of sides for each die, and how many times they will be rolled.
# Then the program displays a table of possible dice sums, the frequency and probability of rolling each of those sums.

import random
rng = random.Random(237)
print()

def throwDice(m, k):
   L = []
   for i in range(m):
      die = rng.randrange(1,k+1)
      L.append(die)
   return tuple(L)


#-- main program --------------------------------------------------------------


dice = int(input("Enter the number of dice: "))
while dice < 1:
   dice = int(input("The number of dice must be at least 1\nPlease enter the number of dice: "))
else:
   print()

sides = int(input("Enter the number of sides on each die: "))
while sides < 2:
   sides = int(input("The number of sides on each die must be at least 2\nPlease enter the number sides on each die: "))
else:
   print()

trials = int(input("Enter the number of trials to perform: "))
while trials < 1:
   trials = int(input("The number of trials must be at least 1\nPlease enter the number of trials to perform: "))
else:
   print()

frequency = (dice*sides+1)*[0]
for i in range(trials):
   result = throwDice(dice, sides)
   if dice == 1:
      frequency[result[0]] += 1
   else:
      frequency[sum(result)] += 1

sums = list(range(dice*sides+1))
probability = dice*[0]
exprobability = dice*[0]
for i in range(dice,len(frequency)):
   probability.append(frequency[i]/trials)
   exprobability.append(probability[i]*100)

print(" Sum{0:5}Frequency{0:5}Relative Frequency{0:5}Experimental Probability".format(" "))
print("----------------------------------------------------------------------")
for i in range(dice, len(frequency)):
   print("{0:>4}{1:>11}{2:>18.5f}{3:>21.2f} %".format(sums[i],frequency[i],probability[i],exprobability[i]))
print()