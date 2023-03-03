def main():
    user_input = input("Input: ")
    word = shorten(user_input)
    print(f"Output: {word}")


def shorten(word):
    s_word = ""
    for c in word:
        if c.lower() not in ["a", "e", "i", "o", "u"]:
            s_word += c
    return s_word



if __name__ == "__main__":
    main()
