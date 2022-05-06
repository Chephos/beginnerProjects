sandwich_orders = ['egg sandwich','pastrami','pastrami','chicken sandwich','pastrami','seafood sandwich','roast beef sandwich','grilled cheese sandwich',
                    'pastrami','ham sandwich','nutella sandwich','pastrami','grilled chicken sandwich']
finished_orders = []
print(f"Deli has run out of Pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
finished_orders += sandwich_orders
print("This is what is available: \n" + ', '.join(finished_orders))
