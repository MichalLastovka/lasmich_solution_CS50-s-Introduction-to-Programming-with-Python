"""
Task:
In a file called emojize.py, implement a program that prompts the user for a str in English and then outputs the “emojized” version of 
that str, converting any codes (or aliases) therein to their corresponding emoji.
"""

from emoji import emojize


def main():
    print("Output:", emojize(get_input()))

def get_input():
    user_input= input("Input: ")
    return user_input

  
if __name__ == "__main__":
    main()
