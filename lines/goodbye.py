# Asking for number

n = int(input("Enter number: "))

lst=[]
# Taking name as input

for i in range n:
    name = input("Enter your name: ")
    lst.append(name)


# printing out the name


for i in range n:
    print(f"Hello {lst[i]}")