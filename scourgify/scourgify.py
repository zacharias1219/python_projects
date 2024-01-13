import csv as c
import sys as s


def main():
    if len(s.argv) < 3:
        s.exit("Too few command-line arguments")
    elif len(s.argv) > 3:
        s.exit("Too many command-line arguments")
    else:
        if s.argv[1][-4:] != ".csv":
            s.exit("Not a CSV file")

    try:
        with open(s.argv[1]) as file:
            read = c.DictReader(file)
            with open(s.argv[2], "w") as file:
                write = c.DictWriter(file, fieldnames=["first", "last", "house"])
                write.writeheader()
                for student_detail in read:
                    last_name, first_name = student_detail["name"].split(", ")
                    house = student_detail["house"]
                    write.writerow({"first": first_name, "last": last_name, "house": house})
    except FileNotFoundError:
        sys.exit(f"Could not read {file}")


if __name__ == "__main__":
    main()
