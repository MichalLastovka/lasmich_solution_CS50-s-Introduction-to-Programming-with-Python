# Task:
# In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, 
# outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.

answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
if answer.lower().strip() == "forty-two" or answer.lower().strip() == "forty two" or answer.strip() == "42":
    print("yes")
else:
    print("no")
