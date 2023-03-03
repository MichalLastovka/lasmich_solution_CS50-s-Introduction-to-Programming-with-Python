# Task:
# In a file called faces.py, implement a function called convert that accepts a str as input and returns that same input with any :) 
# converted to 🙂 (otherwise known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as a slightly frowning face). 
# All other text should be returned unchanged.

def convert(user_text_input):
    smiley = user_text_input.replace(":)", "🙂")
    frowny = smiley.replace(":(", "🙁")

    return frowny

def main():
    user_text_input = str(input("Enter the text: "))
    conversion = convert(user_text_input)
    print(conversion)

main()
