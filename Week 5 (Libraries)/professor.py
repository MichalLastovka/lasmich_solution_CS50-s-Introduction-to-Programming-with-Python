"""
Task:
In a file called professor.py, implement a program that:

- Prompts the user for a level N. If the user does not input 1, 2, or 3, the program should prompt again.
- Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with
  digits. No need to support operations other than addition (+).
- Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and 
  prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after 
  three tries, the program should output the correct answer.
- The program should ultimately output the user’s score: the number of correct answers out of 10.
"""

import random


def main():
    level = get_level()
    score = 0
    problems = 0
    while problems < 10:
        mistakes = 0
        x = generate_integer(level)
        y = generate_integer(level)
        result = x + y
        while mistakes < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == result:
                    score += 1
                    problems += 1
                    break

                elif answer != result and mistakes == 2:
                    print("EEE")
                    problems += 1
                    print(f"{x} + {y} = {result}")
                    break

                elif answer != result and mistakes < 2:
                    print("EEE")
                    mistakes += 1


            except ValueError:
                print("EEE")
                mistakes += 1
                if mistakes > 2:
                    problems += 1
                    print(f"{x} + {y} = {result}")
                    break
                else:
                    pass

    return print("Score:", score)
