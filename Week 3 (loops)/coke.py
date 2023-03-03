"""
Task:
In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the 
amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only 
input integers, and ignore any integer that isn’t an accepted denomination.
"""

def main():
    coins = 0
    price = 50
    while coins < 50:
        print(f"Amount Due: {price}")
        insert = int(input("Insert Coin: "))
        if insert == 5 or insert == 10 or insert == 25:
            coins += insert
            price -= insert
        else:
            pass
    print(f"Change Owed: {coins - 50}")


if __name__ == "__main__":
    main()
