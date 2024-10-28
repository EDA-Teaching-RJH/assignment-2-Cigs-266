### Part Two -- your code goes here. 
import random

#gnerating a random number :))))))
correct_guess = random.randint(1,100)
#tells user what code is about
print("Guess a number between 1 - 100!!!!!!!!!!")
print("I bet you cant guess the same number as me >:3")

#Variable for user input
player_guess = None

#loop until they guess right
while player_guess != correct_guess:
    #ask user for guess
    player_guess = int(input("What am I thinking?? :  "))

#check guess is too high / low
    if player_guess < correct_guess:
        print("Oops!! Too low!!!! Try again >:3")
    elif player_guess > correct_guess:
        print("Oops!! Too high!!!! Try again >:3")
    else:
        print("Congratulations! You guessed the correct number.")

print("Thanks for playing!")

