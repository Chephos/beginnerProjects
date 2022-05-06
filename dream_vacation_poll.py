responses = {}
polling_active = True

while polling_active:
    name = input("What is your name? ")
    response = input("If you could visit one place in the world, where would you go? ")

    responses[name] = response

    again = input("\nWould you like another person to take the poll? (yes/no) ")
    if again == 'no':
        polling_active = False

for name,response in responses.items():
    print(f"{name.title()} will love to visit {response.title()}.")
