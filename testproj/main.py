######################
#                    #
#TESTMMAIN.py        #
#By Michael Carey    #
#Date April 11 2024  #
#Purpose snippits    #
#                    #
######################

import random

#definition of one of our mini games
def hi_low_game():
    #pick a random number between 1 and 10
    hilo_game_number = random.randint(1,10)

    #default our guess before the while loop
    guess = 0

    #while we are still guessing hi or low
    while guess != hilo_game_number:
        #get user input and set it as the variable guess
        guess = int(input("Guess the number between 1-10) :"))

        #check conditions high , low , and , correct guess
        if guess > hilo_game_number and guess < 10:
            print("Guess too high!")
        elif guess < hilo_game_number and guess > 0:
            print("Guess too low!")
        elif guess == hilo_game_number:
            print("You guessed the right number!!")
        else:
            print("Please enter number within range 1-10")

#interface class can be extended to play many games and allows for user input
def interface():

    choice = ""
    while choice != "q":
        choice = input("Would you like to play a game? y/n :")

        if choice == "y":
            hi_low_game()

#main function for the application
def main():
    print("Hi Low GAME!!!!")
    interface()

if __name__ == "__main__":
	main()
