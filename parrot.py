# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt+="\nWhat is your first name? "

# name = input(prompt)
# print(f"\nHello, {name}!")

prompt ="Tell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

message = ""
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)