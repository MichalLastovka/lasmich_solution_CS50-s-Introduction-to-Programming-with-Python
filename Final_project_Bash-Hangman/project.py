""" Created by Michal Lastovka in MAR 2023 for the purpouse of final project to CS50P (Harvard's course of computer science with Python) """

#........................................................IMPORTS...............................................................#
import time
import random
import sys
import json
#........................................................CONSTANTS.............................................................#
EASY = 10
MODERATE = 8
HARD = 7
NIGHTMARE = 6

SHORT = (5, 6)
MEDIUM = (7, 9)
LONG = (10, 11)
EXTRALONG = (12, 15)
#........................................................CLASSES...............................................................#
class TextColor:
    BLUE = '\033[94m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    END = '\033[0m'
#........................................................MAIN..................................................................#
def main():
    menu()
    difficulty = chose_diff()
    word_length = chose_len()
    the_word = pick_word(word_length)
    lifes_left = difficulty
    used_letters = []
    guessed_letters = []
    start = time.time()
    while lifes_left > 0:
        if len(guessed_letters) == len(set(the_word)):
            end = time.time()
            victory(start, end, the_word)
            total_time = end - start
            print(f"\nYour score is: ", count_score(total_time, lifes_left, word_length, difficulty))
            final_menu(the_word)

        print_status(used_letters, guessed_letters, lifes_left, the_word)
        try:
            guess = str(input("Try and guess letters which the word consists of: ")).upper()
            if guess == "" or guess.isalpha() == False or len(guess) > 1:
                print(f"\n{TextColor.RED}⛔ You have to guess a single letter ⛔{TextColor.END}\n")
                pass
            elif guess in the_word and guess not in used_letters:
                print("")
                print(f"{TextColor.GREEN}🍀 Well done, you found one! 🍀{TextColor.END}")
                print("")
                guessed_letters.append(guess)
                used_letters.append(guess)
            elif guess in used_letters:
                print("")
                print(f"{TextColor.YELLOW}⚠️ You have already tried this letter ⚠️{TextColor.END}")
                print("")
            elif guess not in used_letters and guess not in the_word:
                lifes_left -= 1
                used_letters.append(guess)
                print("")
                print(f"{TextColor.RED}⛔ This letter is not in the word ⛔{TextColor.END}")
                print("")

        except ValueError:
            print("")
            print("⚠️ You have to guess a single letter ⚠️")
            print("")
            pass

    defeat(the_word)
    final_menu(the_word)


#........................................................FUNCTIONS.............................................................#
def menu():
    while True:
        try:
            print("")
            print(f"What do you want to do? \n\n{TextColor.GREEN}💥 N for New Game{TextColor.END}\n🫸  {TextColor.RED}Q for Quit{TextColor.END}")
            print("")
            choice = str(input("Action: "))
            if choice.upper() not in ["N", "Q"]:
                print(f"{TextColor.RED}⛔ Invalid choice {TextColor.END}⛔")
                pass
            elif choice.upper() == "N":
                break
            elif choice.upper() == "Q":
                sys.exit(f"{TextColor.GREEN}Thanks for playing!{TextColor.END}⛔\n")
        except ValueError:
            print("H - High Score, N - New Game, Q - Quit: ")
            pass


def chose_diff():
    while True:
        try:
            print("")
            print(f"Choose the difficulty:\n\n🤣  {TextColor.GREEN}E for Easy{TextColor.END}\n🙂  {TextColor.BLUE}M for Medium{TextColor.END}\n😐  {TextColor.YELLOW}H for Hard{TextColor.END}\n😱  {TextColor.RED}N for Nightmare{TextColor.END}")
            print()
            difficulty = str(input("Action: "))
            if difficulty.upper() not in ["E", "M", "H", "N"]:
                print("Invalid choice")
                pass
            if difficulty.upper() == "E":
                return EASY
            if difficulty.upper() == "M":
                return MODERATE
            if difficulty.upper() == "H":
                return HARD
            if difficulty.upper() == "N":
                return NIGHTMARE
        except ValueError:
            print("Enter E - easy, M - moderate, H - hard, N - nightmare: ")
            pass


def chose_len():
    while True:
        try:
            print(f"Choose the length of the word:\n\n🤏  {TextColor.GREEN}S for Short{TextColor.END}\n🖖  {TextColor.BLUE}M for Medium{TextColor.END}\n🤘  {TextColor.YELLOW}L for Long{TextColor.END}\n🤙  {TextColor.RED}E for Extralong{TextColor.END}")
            print()
            length = str(input("Action: "))
            if length.upper() not in ["S", "M", "L", "E"]:
                print("Invalid choice")
                pass
            if length.upper() == "S":
                return SHORT
            if length.upper() == "M":
                return MEDIUM
            if length.upper() == "L":
                return LONG
            if length.upper() == "E":
                return EXTRALONG
        except ValueError:
            print("Enter S - short, M - medium, L - long, E - extralong: ")
            pass


def pick_word(length):
    words = []
    with open("nounlist.csv", "r") as list:
        for row in list:
            if len(row) >= length[0] and len(row) <= length[1] and "-" not in row:
                words.append(row.strip())

    with open("dictionary.json") as json_dict:
        data = json.load(json_dict)
        for word in words:
            if word not in data:
                words.remove(word)

    the_word = random.choice(words)
    return the_word.upper()


def print_status(used_letters, guessed_letters, lifes_left, the_word):
    print(f"{TextColor.BLUE}####################################################################################{TextColor.END}")
    print(f"{TextColor.BLUE}|{TextColor.END}")
    print(f"{TextColor.BLUE}|{TextColor.END} Used letters: ", sorted(used_letters))
    print(f"{TextColor.BLUE}|{TextColor.END}")
    print(f"{TextColor.BLUE}|{TextColor.END} Lifes left: ", "❤️ " * lifes_left)
    print(f"{TextColor.BLUE}|{TextColor.END}")
    print(f"{TextColor.BLUE}|{TextColor.END} Word to guess: ", end="")
    for letter in the_word:
        if letter in guessed_letters:
            print(f" {letter} ", end="")
        else:
            print(" 🗌 ", end="")
    print("")
    print(f"{TextColor.BLUE}|{TextColor.END}")
    print(f"{TextColor.BLUE}####################################################################################{TextColor.END}")
    print("")


def victory(start, end, the_word):

    total_time = round(end - start)
    print("")
    print(f"{TextColor.GREEN}🎉 You won! Congratulations! 🎉{TextColor.END}")
    print("")
    print(f"The word you were looking for is {the_word}.")
    print("")
    print(f"⏱️ Total time: {total_time} seconds ⏱️")


def defeat(the_word):
    print(f"💀 You lost the game, the word you were looking for was {the_word} 💀")
    print("")


def get_definition(the_word):
    with open("dictionary.json") as json_dict:
        data = json.load(json_dict)
        if the_word.lower() not in data:
            return f"Definition of {the_word} not available, check on-line"
        else:
            all_definition = data[f"{the_word.lower()}"]
            if ". 2. " in all_definition:
                definition, _ = all_definition.split(". 2. ")
                return f"{definition.strip()}"
            else:
                return f"{all_definition.strip()}"


def final_menu(the_word):
    while True:
        try:
            print("")
            print("What do you want to do next?")
            print("")
            print(f"{TextColor.GREEN}C for continue the game{TextColor.END}\n{TextColor.BLUE}M for Meaning of the word{TextColor.END}\n{TextColor.RED}Q to Quit the game{TextColor.END}\n")
            choice = str(input("Action: "))
            if choice.upper() not in ["M", "C", "Q"]:
                print("Invalid choice")
            elif choice.upper() == "Q":
                print("")
                sys.exit("Thanks for playing")
            elif choice.upper() == "C":
                main()
            elif choice.upper() == "M":
                print("")
                print(get_definition(the_word))
                print("")

        except ValueError:
            print("Invalid choice")
            pass


def count_score(total_time, lifes_left, word_length, difficulty):
    win_score = 100
    time_score = total_time
    lifes_score = lifes_left * 10
    word_score = 0
    if word_length == (5, 6):
        word_score += 20
    elif word_length == (7, 9):
        word_score += 10
    elif word_length == (10, 11):
        word_score += 5
    elif word_length == (12, 15):
        word_score += 0
    difficulty_score = 0
    if difficulty == 10:
        difficulty_score += 0.8
    elif difficulty == 8:
        difficulty_score += 1
    elif difficulty == 7:
        difficulty_score += 1.2
    elif difficulty == 6:
        difficulty_score += 1.8

    return round((win_score - time_score + lifes_score + word_score) * difficulty_score)


#........................................................SCRIPT................................................................#
if __name__ == "__main__":
    main()
