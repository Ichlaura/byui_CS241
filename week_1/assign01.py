# Lewis Lockhart :: CS-241
import random
from random import randint


# allows for alternate color usage in the console
class Color:
    BLUE = '\033[1;34;48m'
    GREEN = '\033[1;32;48m'
    YELLOW = '\033[1;33;48m'
    RED = '\033[1;31;48m'
    END = '\033[1;37;0m'


# greeting
print(Color.GREEN + "Welcome to the number guessing game!" + Color.END)
# get the seed value from user input
seed_value = input("Enter random seed: ")
# for the testBed to predict what your random numbers will be
random.seed(seed_value)

# variables
rand_num = 0
user_guess = 0
num_guesses = 0


# get number guess from the user
def get_user_guess():
    guess = int(input(Color.BLUE + "\nPlease enter a guess: " + Color.END))
    global user_guess
    user_guess = guess


# provide feedback to the user for high and low
def high_or_low():
    global user_guess
    global rand_num
    # if user guess is too low
    if user_guess < rand_num:
        print("Higher")
    # if user guess is too high
    elif user_guess > rand_num:
        print("Lower")


# resets numbers prior to starting a new game
def reset_nums():
    global user_guess
    global num_guesses
    user_guess = 0
    num_guesses = 0


# runs the basic game code
def play_game():
    global rand_num
    max_low = 1
    max_high = 100
    rand_num = randint(max_low, max_high)

    global num_guesses
    get_user_guess()
    high_or_low()
    num_guesses += 1

    while user_guess != rand_num:
        get_user_guess()
        high_or_low()
        num_guesses += 1

    if user_guess == rand_num:
        win()


# prompts, calls play_game, or ends game
def play_again():
    valid_yes = ["yes", "Yes", "YES"]
    valid_no = ["no", "No", "NO"]
    # get user input
    response = input("\nWould you like to play again (yes/no)? ")
    # if yes
    if response in valid_yes:
        reset_nums()
        play_game()
    # if no
    elif response in valid_no:
        print("Thank you. Goodbye.")
        exit()
    # if invalid
    else:
        raise Exception("Invalid response: options are 'yes' or 'no'.")


# provides feedback to the player if they win
def win():
    print(Color.YELLOW + "Congratulations. You guessed it!" + Color.END)
    print("It took you " + Color.BLUE + f"{num_guesses}" + Color.END + " guesses.")
    play_again()


# triggers the beginning of the game
play_game()
