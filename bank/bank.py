def main():
    greeting = input("Greeting: ").lower().strip()
    greeting = value(greeting)
    print(f"${greeting}")


def value(greet):
    if greet.startswith("hello"):
        return 0
    elif greet.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()