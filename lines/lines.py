import sys as s


def main():
    if len(s.argv) < 2:
        s.exit("Too few command-line arguments")
    elif len(s.argv) > 2:
        s.exit("Too many command-line arguments")
    else:
        if s.argv[1][-3:] != ".py":
            s.exit("Not a python file")

    try:
        count_lines = 0
        with open(s.argv[1], "r") as file:
            for line in file:
                if not (line.lstrip().startswith("#") or line.strip() == ""):
                    count_lines += 1
            print(count_lines)
    except FileNotFoundError:
        s.exit("File does not exist")


if __name__ == "__main__":
    main()
