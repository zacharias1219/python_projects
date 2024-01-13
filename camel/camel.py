name = input("camelCase: ")
print("snake_case: ",end="")
for i in name:
    if(i.isupper()):
        print("_",end="")
    print(i.lower(),end="")
print("\n")