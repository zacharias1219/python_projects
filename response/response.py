import validators as va


def main():
    email = input("What's your email address? ")
    validated_email = validate(email)
    print(validated_email)


def validate(email):
    if va.email(email) == True:
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
