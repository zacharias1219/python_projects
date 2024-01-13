from datetime import date
import inflect as i

p = i.engine()
import sys as s
import operator as o


def main():
    try:
        DOB = input("Date of Birth: ")
        time = o.sub(date.today(), date.fromisoformat(DOB))
        print(convert(time.days))
    except ValueError:
        s.exit("Invalid date")


def convert(time):
    minutes = time * 24 * 60
    return f"{(p.number_to_words(minutes, andword='')).capitalize()} minutes"


if __name__ == "__main__":
    main()
