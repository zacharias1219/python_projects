import re as r


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip_address):
    if r.search("^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip_address):
        numbers_list = ip_address.split(".")
        for number in numbers_list:
            num = int(number)
            if num < 0 or num > 255:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
