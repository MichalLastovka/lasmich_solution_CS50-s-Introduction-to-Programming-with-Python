"""
Task:
In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding 
name in snake case. Assume that the user’s input will indeed be in camel case.
"""

def main():
    camelCase = input("camelCase: ")
    snake_case = ""
    for c in camelCase:
        if c.islower():
            snake_case += c
        else:
            snake_case += f"_{c.lower()}"
    print(snake_case)




if __name__ == "__main__":
    main()
