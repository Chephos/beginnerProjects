usernames=[]
current_users = ['Jordan','Efosa','Dandy', 'Faith','Admin','Chidozie','Kelechi','Hot-zed']
current_users_lower = ['jordan','efosa','dandy', 'faith','admin','chidozie','kelechi','hot-zed']
new_users = ['Ephy','Jobby','Oreistired','Efosaisfedup', 'Dandy', 'Jordan','chidozie']
for new_user in new_users:
    if (new_user in current_users) or (new_user in current_users_lower):
        print(f"{new_user} already taken, kindly enter a new username")
    else:
        print(f'{new_user} is available for use.')
        usernames.append(new_user)
if usernames:
    for username in usernames:
        if username == 'Admin':
            print(f"Hello {username}, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")
else:
    print('We need to find some users!')




