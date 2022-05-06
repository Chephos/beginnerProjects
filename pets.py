# pet1 = {
#     'pet':'dog',
#     'owner':'Efosa'
# }
# pet2 = {
#     'pet':'cat',
#     'owner':'fire',
# }
# pet3 = {
#     'pet':'hamster',
#     'owner':'omotola',
# }
# pet4 = {
#     'pet':'cat',
#     'owner':'duke',
# }
# pet5 = {
#     'pet':'dog',
#     'owner':'folusho',
# }

# pets = [pet1,pet2,pet3,pet4,pet5]

# for pet in pets:
#     print(f"{pet['owner'].title()} owns a {pet['pet'].title()}")

favorite_places = {
    'david':['mko stadium','unilag','backyard grillz'],
    'seun':['paris'],
    'tobi':['london','lekki','data first'],
}

for name,place in favorite_places.items():
    if len(place) > 1:
        print(f"{name.title()}'s favorite places are {', '.join(place)}")
    else:
        print(f"{name.title()}'s favorite place is {''.join(place)}")
# for name,places in favorite_places.items():
#     for place in places:
#         print(f"{name}'s favorite place(s) is/are {place}") 

