#Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20. 
import random
print("Hello! What is your name?")
a=string=input()
print("Well,", a,", I am thinking of a number between 1 and 20.")
print("Take a guess.")
x=random.randrange(1, 20)
cnt=1
while True:
    y=int(input())
    if not y:
        break
    if y<x:
        print("Your guess is too low.")
        print("Take a guess.")
        cnt +=1
    elif y>x:
        print("Your guess is too high.")
        print("Take a guess")
        cnt+=1
    else:
        print("Good job,", a,"! You guessed my number in", cnt, "guesses!")
        break