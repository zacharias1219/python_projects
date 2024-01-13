import re as r


def main():
    text = input("Text: ")
    counted = count(text)
    print(counted)


def count(text):
    lowered_text = text.lower()
    n_um_ber = r.findall("(^|\W)um($|\W)", lowered_text)
    return len(n_um_ber)


if __name__ == "__main__":
    main()
