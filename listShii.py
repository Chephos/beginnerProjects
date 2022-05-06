# squares = []
# for value in range(1,11):
#     squares.append(value**2)
# print(squares)

# squares = [value**2 for value in range(1,11)]
# print(squares)

# for number in range(1,21):
#     print(number)
# millions = list(range(1,1_000_001))
# # for million in millions:
# #     print(million)
# print(min(millions))
# print(max(millions))
# print(sum(millions))
# odd_numbers = list(range(1,21,2))
# for odd in odd_numbers:
#     print(odd)
# for x in list(range(3,31,3)):
#     print(x)
# cubes= []
# for cube in range(1,11):
#     cubes.append(cube**3)
# print(cubes)

# cubes =[cube**3 for cube in range(1,11)]
# print(cubes)

players = ['charles','martina','micheal','florence','eli']
print('Here are the first three players on my team:')
for player in players[:3]:
    print(player.title())
