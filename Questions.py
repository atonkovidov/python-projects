# Andre Tonkovidov
# atonkovidov@ucsc.edu
# pa5
# The program guesses a number that the user picks from a range of two, user-provided
# numbers and states how many guesses it took to make the correct guess.

def question(a):
   print()
   print("Is your number Less than, Greater than, or Equal to", str(a)+"?")
   answer = input("Type \'L\', \'G\' or \'E\': ")
   while answer not in ['E','G','L','e','g','l']:
      print()
      answer = input("Please type \'L\', \'G\', \'E\': ")
   else:
      return answer

def search(low,high):
   guesses = 0
   while low <= high:
      middle = (low + high)//2
      if low == high:
         return guesses,middle
      else:
         answer = question(middle)
         guesses += 1
         if answer in ['g', 'G']:
            low = middle + 1
         elif answer in ['l', 'L']:
            high = middle - 1
         else:
            return guesses,middle
   print()
   print("Your answers have not been consistent.\n\n")
   exit(0)
         
         
#-- main program --------------------------------------------------------------


print()
print()
print("Enter two numbers, low then high.")
low = int(input("low = "))
high = int(input("high = "))
guesses = 0

while low > high:
   print()
   print("Please enter the smaller followed by the larger number.")
   low = int(input("low = "))
   high = int(input("high = "))

print()
print("Think of a number in the range", str(low), "to", str(high)+".")
guesses,middle = search(low,high)
print()

if guesses == 1:
   print("I found your number in 1 guess.")
else:
   print("Your number is", str(middle)+". I found it in", str(guesses),"guesses.")
print()
print()