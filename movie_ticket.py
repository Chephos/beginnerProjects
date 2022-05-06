prompt = "\nHow old are you? "
while True:
    age = int(input(prompt))
    cost = 0
    out = ''
    if age == 00:
        break
    if age < 3:
        int(age)
        cost = 0
        print("Your ticket is free!")
    elif age < 12:
        cost = 10
        print(f"Your ticket costs ${cost}")
    elif age > 12:
        cost = 15
        print(f"Your ticket costs ${cost}")
