for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print ("CracklePop")
        continue
    elif number % 3 == 0:
        print("Crackle")
        continue
    elif number % 5 == 0:
        print ("Pop")
        continue
    else: print(number)