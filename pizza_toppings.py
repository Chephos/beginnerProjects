prompt = "\nEnter any pizza topping of your choice"
prompt += "\n(Enter 'quit' to exit:) "

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"I'll add {topping.title()} to your pizza!")


