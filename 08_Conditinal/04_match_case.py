a = int(input("Enter  a Number Between 1 to 10: "))

match a:
    case 1:
        print("You won Charger")
    case 3:
        print("You won $3")
    case 6:
        print("You won a camera")
    case _:
        print("Better luck Next Time")