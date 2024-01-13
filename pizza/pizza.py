import csv as c
import sys as s
from tabulate import tabulate

def main():
    if len(s.argv) < 2:
        s.exit("Too few command-line arguments")
    elif len(s.argv) > 2:
        s.exit("Too many command-line arguments")
    else:
        if s.argv[1][-4:] != ".csv":
            s.exit("Not a CSV file")

    try:
        with open(s.argv[1]) as file:
            tabulated_pizza = tabulate(c.reader(file), headers="firstrow", tablefmt="grid")
            print(tabulated_pizza)
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()