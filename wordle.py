# Wordle (Python Version)
#
# Details
# This game is a classic game that has recently blown up in 2022
# This game gives you 6 tries to guess a secret word
#
# Author: Jovian Kuntjoro

# Import the necessary functions and variables
from words import guess_words, valid_words
import random as rn
from time import sleep as slp
from os import system, name
from sys import stdout as std
from termcolor import colored as cl

# Initialize the list to store the colour results and the guessed words
color_list = []
guess_list = []

# Initialize the all-important guessed boolean
guessed = False

# Function to compare the two words, returning "green" for same, "yellow" for wrong place, and "white" for not at all;
def compare(guessed_word, cur_word):

    # Initialize the result array
    res = []

    # Initialize the taken array
    taken = [False, False, False, False, False]

    # Initialize guessed as true
    global guessed
    guessed = True

    # Loop through each letter
    for i in range(5):
        if guessed_word[i] == cur_word[i] and not taken[i]:

            # The letter is in the right place
            res.append("green")

            # That letter is taken
            taken[i] = True
        else:

            # Check if the letter is anywhere else in the word
            for j in range(5):
                if guessed_word[i] == cur_word[j] and not taken[j]:
                    if guessed_word[j] == cur_word[j]:
                        continue

                    # The letter is there, but in the wrong space
                    res.append("yellow")
                    guessed = False

                    # That letter is taken
                    taken[j] = True

                    # No longer check the same letter anymore
                    break

                if j == 4:

                    # The letter is not in the word at all
                    res.append("white")
                    guessed = False

    # Record the results
    record_result(res, guessed_word)

    # Function is successful
    return 0

# Function to record the results of compare()
def record_result(res, guessed_word):
    clear()

    # Append the results to the memory list
    guess_list.append(guessed_word)
    color_list.append(res)

    # Print the memory list
    print_prev_words(color_list, guess_list)

    # Function is successful
    return 0

# Function to print the previous guesses
def print_prev_words(colours, guesses):
    clear()

    # For every word in the memory list, print them with the according colours
    for i in range(len(colours)):
        for j in range(len(colours[i])):
            print(cl(guesses[i][j], colours[i][j]), end="")
        print("")
    print("")

    # Function is successful
    return 0


# Function to validate if the guessed word is valid (in the word list)
def validate(words, cur_word, guesses):

    # Repeats until the guess is valid
    while True:
        print(f"You have {guesses} guesses left.")
        print("Make your guess:")

        # Take the player's guess
        guessed_word = input().lower()

        # Check if the guessed word is in the word list
        if guessed_word in words:
            compare(guessed_word, cur_word)
            break
        else:
            print("Not a valid 5 letter word.")
            slp(2)
            delete_last_lines(4)
        
    # Function is successful
    return 0

# Function that deletes "number" last lines
def delete_last_lines(number):
    for i in range(number):

        # Move cursor up
        std.write("\x1b[1A")

        # Delete current line
        std.write("\x1b[2K")

    # Function is successful
    return 0

# Function to clear the whole output
def clear():

    # Check whether device is Windows
    if name == "nt":
        system("cls")
    else:
        system("clear")

    # Function is successful
    return 0

# Main function for the Wordle
def main():

    # Get the global guessed variable
    global guessed

    # Print introduction for the game
    clear()
    print("Hello, welcome to Python Wordle!")
    slp(2)
    print("\nWould you like to know how to play? If yes, type 'yes'. If no, type anything else")

    # Get user input to print instructions or not
    user_input = input().lower()
    clear()

    # If user agrees, print instructions
    while user_input == "yes":
        print("Here is how to play:")
        print("\nYou have 6 tries to guess a random 5 letter word.")
        print("When a letter is green, it means that the letter is in the correct spot.")
        print("When a letter is yellow, it means that the letter is in the wrong spot, but is inside the secret word.")
        print("When a letter is white, it means that the letter is not in the secret word at all.")
        slp(5)
        print("\nType anything to continue")

        # Check if user understands
        user_input = input().upper()

    # Set to "yes" to enter while loop
    user_input = "yes"

    # Plays again until user says no
    while user_input == "yes":
        clear()

        # Pick a random word to be the secret word
        words = guess_words
        cur_word = rn.choice(words)
        words.extend(valid_words)

        # Clear the memory list if it is not empty already
        guess_list.clear()
        color_list.clear()

        # Initialize the necessary variables
        guessed = False
        guesses = 6

        # Asks for player to guess until word is guessed or guesses run out
        while guesses > 0 and guessed == False:
            validate(words, cur_word, guesses)
            guesses -= 1

        # Check whether the person guessed the word or ran out of guesses
        if guessed == True and guesses >= 0:
            print("You guessed the word!")
            slp(2)
            print(f"You guessed the word in {6 - guesses} guesses!")
        elif guesses == 0 and guessed == False:
            print("You ran out of guesses!")
            slp(2)
            print(f"The word was {cur_word}.")

        slp(2)

        # Invite user to play again
        print("\nPlay again? Say 'yes' to restart and anything else to quit.")
        user_input = input().lower()

    return 0

# To call main function
if __name__ == "__main__":
    main()