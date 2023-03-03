"""
Task:
In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d 
(which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically 
by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input 
case-insensitively.
"""


def main():
    shopping_list = {}
    while True:
        try:
            item = get_input()
            if item in shopping_list:
                shopping_list[item] += 1
            else:
                shopping_list[item] = 1

        except EOFError:
            sorted_list = dict(sorted(shopping_list.items()))
            for item in sorted_list:
                print(sorted_list[item], item.upper())
            break

def get_input():
    item = str(input(""))
    return item


if __name__ == "__main__":
    main()
