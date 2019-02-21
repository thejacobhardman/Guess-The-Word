# Jacob Hardman
# Intro To Programming
# Professor Marcus Longwell
# 2/13/19
# Python Version 3.7.2

# Importing the 'random' pkg
import random

###################################################### GLOBAL VARIABLES ##################################################################

# List of answers based on difficulty
Easy_Words = ["BOOK", "HELP", "POPE", "DOOR", "SHOW", "POOR", "LORD", "SHOP"] # 4 letter words
Medium_Words = ["STORE", "FLOOR", "BOARD", "TRACE", "BRACE", "TRASH", "FLASH"] # 5 letter words
Hard_Words = ["SECURITY", "PASSWORD", "DATABASE", "HACKER"] # More than 5 letter words

Game_State = False # Tracks the game state

Guessed_Letters = [] # Tracks the letters that the player has guessed

######################################################### GAME LOGIC #####################################################################

def Easy_Difficulty(): # The player guesses 4 letter words

    # Generating the answer
    Answer = random.choice(Easy_Words)

    # Debug Statements
    # print(Answer)

    print("\n")

    while Game_State == True:

        Hint = "" # resets the hint to prevent the hint from getting too long

        for character in Answer: # Checks each character in the answer against the list of guessed letters
            if character.upper() in Guessed_Letters:
                Hint = Hint + character
            else:
                Hint = Hint + "*"

        print(Hint.center(100, " ")) # Prints out a hint

        Ask_Player = input("\nWould you like to guess the word? (y/n): ")

        if Ask_Player == "y": # The player will attempt to guess the word
            Final_Guess = input("\nPlease enter your guess: ")
            if Final_Guess.upper() == Answer:
                print("YOU WIN!\n".center(102, " "))
                break
            else:
                print("Wrong. Try again.\n".center(100, " "))
        elif Ask_Player == "n": # The player would rather guess a letter
            Letter_Guess = input("\nPlease guess a letter: ")
            if Letter_Guess.upper() in Answer:
                print("That letter is in the word.")
                Guessed_Letters.append(Letter_Guess.upper())
            else:
                print("That letter is not in the word.")
                Guessed_Letters.append(Letter_Guess.upper())

def Medium_Difficulty(): # The player guesses 5 letter words

     # Generating the answer
    Answer = random.choice(Medium_Words)

    # Debug Statements
    # print(Answer)

    print("\n")

    while Game_State == True:

        Hint = "" # resets the hint to prevent the hint from getting too long

        for character in Answer: # Checks each character in the answer against the list of guessed letters
            if character.upper() in Guessed_Letters:
                Hint = Hint + character
            else:
                Hint = Hint + "*"

        print(Hint.center(100, " ")) # Prints out a hint

        Ask_Player = input("\nWould you like to guess the word? (y/n): ")

        if Ask_Player == "y": # The player will attempt to guess the word
            Final_Guess = input("\nPlease enter your guess: ")
            if Final_Guess.upper() == Answer:
                print("YOU WIN!\n".center(102, " "))
                break
            else:
                print("Wrong. Try again.\n".center(100, " "))
        elif Ask_Player == "n": # The player would rather guess a letter
            Letter_Guess = input("\nPlease guess a letter: ")
            if Letter_Guess.upper() in Answer:
                print("That letter is in the word.")
                Guessed_Letters.append(Letter_Guess.upper())
            else:
                print("That letter is not in the word.")
                Guessed_Letters.append(Letter_Guess.upper())

def Hard_Difficulty(): # The player guesses words with more than 5 letters

    # Generating the answer
    Answer = random.choice(Hard_Words)

    # Debug Statements
    # print(Answer)

    print("\n")

    while Game_State == True:

        Hint = "" # resets the hint to prevent the hint from getting too long

        for character in Answer: # Checks each character in the answer against the list of guessed letters
            if character.upper() in Guessed_Letters:
                Hint = Hint + character
            else:
                Hint = Hint + "*"

        print(Hint.center(100, " ")) # Prints out a hint

        Ask_Player = input("\nWould you like to guess the word? (y/n): ")

        if Ask_Player == "y": # The player will attempt to guess the word
            Final_Guess = input("\nPlease enter your guess: ")
            if Final_Guess.upper() == Answer:
                print("YOU WIN!\n".center(102, " "))
                break
            else:
                print("Wrong. Try again.\n".center(100, " "))
        elif Ask_Player == "n": # The player would rather guess a letter
            Letter_Guess = input("\nPlease guess a letter: ")
            if Letter_Guess.upper() in Answer:
                print("That letter is in the word.")
                Guessed_Letters.append(Letter_Guess.upper())
            else:
                print("That letter is not in the word.")
                Guessed_Letters.append(Letter_Guess.upper())

######################################################### GAME FLOW ######################################################################

print("Welcome to guess the word!\nPlease select your difficulty.")

# this loop will run until the user inputs a correct value in order to choose a difficulty
while Game_State == False:

    Select_Difficulty = input("Enter '1' for Easy Difficulty, enter '2' for Medium Difficulty, or enter '3' for Hard Difficulty: ")

    if int(Select_Difficulty) == 1: # The player selected the 'Easy_Difficulty' function
        Game_State = True
        Easy_Difficulty()
        break
    elif int(Select_Difficulty) == 2: # The player selected the 'Medium_Difficulty' function
        Game_State = True
        Medium_Difficulty()
        break
    elif int(Select_Difficulty) == 3: # The player selected the 'Hard_Difficulty' function
        Game_State = True
        Hard_Difficulty()
        break
    else:
        print("I'm sorry, I don't understand what you mean.\n")

# Execute this logic after the game is over
input("Thanks for playing! Press 'enter' to close the program.")
