groceries = {}
while True:
    try:
        item = input().lower()
        if item in groceries:
            groceries[item]+=1
        else:
            groceries[item] = 1
    except EOFError:
        for i in sorted(groceries.keys()):
            print(groceries[i],i.upper())
        break