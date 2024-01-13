sol = input("What is the Answer to the Great Question of life, the Univese, and Everything? ").lower().strip()
match sol:
    case '42' | 'forty-two' | 'forty two':
        print("Yes")
    case _:
        print("No")
