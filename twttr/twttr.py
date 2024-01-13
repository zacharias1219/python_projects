def main():
    text = input("Input: ")
    output = shorten(text)
    print(f"Output: {output}")


def shorten(word):
    shortened = ""
    for c in word:
        if c.lower() not in ["a", "e", "i", "o", "u"]:
            shortened+=c
    return shortened


if __name__ == "__main__":
    main()