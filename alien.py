# # alien_0 = {'color':'green','points':5}
# # print(alien_0)
# # new_points = alien_0['points']
# # print(f"You've just earned {new_points} points!")
# # alien_0['x_position'] = 0
# # alien_0['y_position'] = 25
# # print(alien_0)

# alien_0 = {}

# alien_0['color'] = 'green'
# alien_0['points'] = 5

# print(alien_0)
# alien_0 = {'color':'green','points':5}
# print(f"The alien is {alien_0['color']}.")

# alien_0['color'] = 'yellow'
# print(f"The alien is now {alien_0['color']}")

# alien_0 = {'x_position':0,'y_position':25, 'speed':'medium'}
# # print(f"Original position: {alien_0['x_position']}")

# # #Move the alien to the right.
# # #Determine how far to move the alien based on it's current speed.
# # if alien_0['speed'] == 'slow':
# #     x_increment = 1
# # elif alien_0['speed'] == 'medium':
# #     x_increment = 2
# # else:
# #     #this must be a fast alien.
# #     x_increment = 3

# # # the new position is the old position plus the increment.
# # alien_0['x_position'] = alien_0['x_position'] + x_increment

# # print(f"New position: {alien_0['x_position']}")
# print(alien_0)

# del alien_0['speed']
# print(alien_0)


# language = favorite_languages['sarah'].title()
# print(f'sarah\'s favorite language is {language}.')
# point_value =  favorite_languages.get('chike', 'Chike has no favorite language assigned')
# print(point_value)

# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")

# for name in favorite_languages.keys():
#     print(f"\n{name.title()}")

# for name in favorite_languages:
#     print(name.upper())

# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(name.title())

#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}")

# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll.")

favorite_languages = {
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward': ['ruby','go'],
    'phil': ['python', 'haskell'],
}

for name,languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite languages are:")
    else:
        print(f"\n{name.title()}'s favorite language is:")
    for language in languages:
        print(f"\t{language.title()}")
proposed_candidates = [
    'tola','jerry','edward','itunu','jaspa','ade','bola','jen','faraday','segun','sarah'
]

# for candidate in proposed_candidates:
#     if candidate in favorite_languages.keys():
#         print(f"Thank you {candidate.title()} for responding!")
#     else:
#         print(f"Kindly take the poll.")