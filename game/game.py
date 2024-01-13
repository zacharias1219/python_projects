import random as r

while True:
    try:
        bound = int(input("Level: "))
        if bound > 0:
            break
    except:
        pass

random_numb = r.randint(1, bound)

while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0 and guess <= bound:
            if guess < random_numb:
                print("Too small!")
            elif guess > random_numb:
                print("Too large!")
            else:
                print("Just right!")
                break
    except:
        pass
