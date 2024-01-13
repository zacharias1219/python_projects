names_list = []

while True:
    try:
        name = input("Name: ").title()
        names_list.append(name)
    except EOFError:
        print()
        if len(names_list) == 1:
            print(f"Adieu, adieu, to {names_list[0]}")
        elif len(names_list) == 2:
            print(f"Adieu, adieu, to {names_list[0]} and {names_list[1]}")
        else:
            print("Adieu, adieu, to ", end="")
            for i in range(len(names_list)):
                if i == len(names_list) - 1:
                    print(f"and {names_list[-1]}")
                    break
                print(f"{names_list[i]}, ", end="")
        break
