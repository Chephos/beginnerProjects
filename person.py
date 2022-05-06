
# favorite_numbers = {
#     'Efosa':[0, 6,2],
#     'Ofun':[9, 17,0],
#     'David':[12,13,9],
#     'Pelzz':[4,8],
#     'Esohe':[6,4,5]
# }
# for name,numbers in favorite_numbers.items():
#     print(f"{name}'s favorite numbers are: ")
#     for number in numbers:
#         print(f"{number}")
#     print()

# print(f"Efosa's favorite number is {favorite_numbers['Efosa']}")
# print(f"Ofun's favorite number is {favorite_numbers['Ofun']}.")

# user_0 = {
#     'username':'efermi',
#     'first':'enrico',
#     'last':'fermi',
# }

# for key, value in user_0.items():
#     print(f"\nKey: {key}")
#     print(f"Value: {value}")

# rivers = {'nile':'egypt','niger':'nigeria','benue':'benue',}

# # for river, location in rivers.items():
# #     print(f"The {river.title()} runs through {location.title()}")

# for river in rivers:
#     print(river)

# for location in rivers.values():
#     print(location.title())

# person1 = {
#     'first_name':'Chinasa',
#     'last_name':'Ezeh',
#     'city':'Chi town',
#     'age':20,    
#     }

# person2 = {
#     'first_name':'chioma',
#     'last_name':'okanu',
#     'city':'london',
#     'age':20,
# }

# person3 = {
#     'first_name':'kolade',
#     'last_name':'oluwadara',
#     'city':'north-hampton',
#     'age':20,
# }

# people = [person1,person2,person3]
# for person in people:
#     print(f"{person['first_name'].title()} {person['last_name'].title()} is" 
#         f" {person['age']} years old and is proudly {person['city']}" )

from math import factorial


cities = {
    'lagos':{
        'country':'Nigeria',
        'population':14_862_000,
        'fact':'It is a land where dreams come true'
    },
    'new york':{
        'country':'USA',
        'population':8_419_000,
        'fact':'New Yorkers bite 10 times more ' 
                'people than sharks do worldwide each year.'
    },
    'chicago':{
        'country':'USA',
        'population':2_710_000,
        'fact':"The first US blood bank"
    },
}

for city,details in cities.items():
    print(f"\n{city.title()} has the following details")
    country = f"{details['country']}"
    population = f"{details['population']}"
    fact = f"{details['fact']}"

    print(f"\tCountry: {country}")
    print(f"\tPopulation: {population}")
    print(f"\tRandom fact: {fact}")