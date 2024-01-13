def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if (len(s)>6 or len(s)<2):
        return False
    if (s[0].isalpha() == False or s[1].isalpha() == False):
        return False
    for i in s:
        if (i.isalpha() == False):
            if (s[len(s)-1].isalpha() == True or s[len(s)-2].isalpha() == True):
                return False
    for i in s:
        if (i.isalpha() == False):
            if i == '0':
                return False
            else:
                break
    for i in s:
        if  (i == '.' or i == ' ' or i == '!' or i == '?'):
            return False
    return True

if __name__ == "__main__":
    main()