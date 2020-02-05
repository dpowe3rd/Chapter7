sandwich_orders = ['turkey and cheese', 'roast beef', 'chicken', 'chopped cheese']
finished_sandwiches = []

while sandwich_orders:
    order = sandwich_orders.pop()

    print('We have made your ' + order + ' sandwich, please pick it up at the counter.')
    finished_sandwiches.append(order)

print('\n')

while finished_sandwiches:
    finshedfood = finished_sandwiches.pop()
    print(finshedfood)
