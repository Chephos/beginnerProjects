#moving items from one list to another
sandwich_orders = ['egg sandwich','chicken sandwich','seafood sandwich','roast beef sandwich','grilled cheese sandwich'
                    'ham sandwich','nutella sandwich','grilled chicken sandwich']
finished_sandwich = []

while sandwich_orders:
    attended_orders = sandwich_orders.pop()
    print(f"I made your {attended_orders}.")
    finished_sandwich.append(attended_orders)

for sandwich in finished_sandwich:
    print(f"{sandwich.title()} was made.")