"""
Task:
In a file called game.py, implement a program that:
Prompts the user for a level, N. If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and N inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.

    If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
    If the guess is larger than that integer, the program should output Too large! and prompt the user again.
    If the guess is the same as that integer, the program should output Just right! and exit.
    
"""

import random

def main():
    num = get_num()
    while True:
        guess = get_guess()
        if guess == num:
            print("Just right!")
            break
        elif guess > num:
            print ("Too large!")
            pass
        else:
            print("Too small!")
            pass

def get_num():
    while True:
        try:
            n = int(input("Level: "))
            num = random.randint(1, n)
            return num
        except ValueError:
            pass

def get_guess():
    while True:
        try:
            guess = int(input("Guess: "))
            return guess
        except ValueError:
            pass


if __name__ == "__main__":
    main()
