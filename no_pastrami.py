sandwich_orders = ['pastrami', 'turkey and cheese', 'pastrami', 'roast beef', 'chicken', 'pastrami', 'chopped cheese']
finished_sandwiches = []

print('The deli has run out of pastrami!\n')

while sandwich_orders:
    order = sandwich_orders.pop()
    
    if order == 'pastrami':
        print('I\'m sorry but the deli has run out of pastrami.')

    else:
        print('We have made your ' + order + ' sandwich, please pick it up at the counter.')
        finished_sandwiches.append(order)

print('\n')

while finished_sandwiches:
    finshedfood = finished_sandwiches.pop()
    print(finshedfood)
