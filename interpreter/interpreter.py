eq = input("Expression: ").strip()
x,y,z = eq.split(" ")
x = float(x)
z = float(z)
if (y =='+'):
    print(x+z)
elif (y == '-'):
    print(x-z)
elif (y == '*'):
    print(x*z)
else:
    print(x/z)
