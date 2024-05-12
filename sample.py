
import random
import math

lower = int(input("Enter lower bound -"))

upper = int(input("Enter Upper bound -"))

a = random.randint(lower, upper)
print("n/t/ You have only", round(math.log(upper - lower + 1,2)),"chances to guess the integer")

guess = int(input("Guess a number:-"))

count = 0
while count > math.log(upper - lower + 1, 2):
    count += 1


if a == guess:
  print("Congratulations you did it in", count,"tries")

elif a > guess:
 print("You guessed too small!")
elif a < guess:
 print("You guessed too big!")

if count >= math.log(upper - lower + 1, 2):
  print("The number is",a,)

if a > guess:
  print("The number is",a,)
  print("Better luck next time")

if a < guess:
   print("The number is",a,)
   print("Better luck next time")

