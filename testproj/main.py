######################
#                    #
#TESTMMAIN.py        #
#By Michael Carey    #
#Date April 11 2024  #
#Purpose snippits    #
#                    #
######################

import random
import os

def password_gen(passwd_size):
    
    password = ""
    special_chars ="!@#$%^&*()-_=+[]{}~?<>"
    lower_case = "qwertyuiopasdfghjklzxcvbnm"
    upper_case = "QWERTYUIOPASDFGHJKLZXCVBNM"
    nums ="1234567890"
    count =0

    while count <= passwd_size:

        password += special_chars [random.randint(0, len(special_chars) -1    )       ]
        password += lower_case    [random.randint(0, len(lower_case)    -1    )       ]
        password += upper_case    [random.randint(0, len(upper_case)    -1    )       ]
        password += nums          [random.randint(0, len(nums)          -1    )       ]
        count = count +1

    password = password[:passwd_size]
    
    print("Generated Password: "+ password)


#definition of one of our mini games
def hi_low_game():
    
    invalid_chars = "qwertyuiop`~-=_+asdfghjkl;:'""zxcvbnm,<.>/?[]{}\|"
    invalid_char_detetced = False
    #pick a random number between 1 and 10
    hilo_game_number = random.randint(1,10)

    #default our guess before the while loop
    guess = 0

    #while we are still guessing hi or low
    while guess != hilo_game_number:
        #get user input and set it as the variable guess
        guess = input("Guess the number between 1-10) :")

        #filter out bad input
        for char in invalid_chars:
            if guess.__contains__(char):
                invalid_char_detetced = True

        if guess == '' or invalid_char_detetced:
            print("Invalid input please try again")
        else:
            guess = int(guess)
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
        choice = input("Would you like run a program? y/n/q :")

        if choice == "y":
            program = input("Choose a program 1 High Low Game 2 Password Generator: ")
            match program:
                case "1":
                    hi_low_game()
                case "2":
                    #password generator
                    length = input("Password Length: ")
                    password_gen(int(length))
                case _:
                    print("invalid option")

#main function for the application
def main():
    print("Hi Low GAME!!!!")
    interface()

if __name__ == "__main__":
	main()
