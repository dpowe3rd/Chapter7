vacation = {}

polling = True

while polling:
    name = input('\nWhat is your name? ')
    response = input('Where is your dream vacation, ' + name + '. ')

    vacation[name] = response

    again = input('Would you like to let someone else use the poll? Please input yes or no. ')
    if again.lower() == 'no':
        polling = False

print('\n---Results of the Poll---\n')
for person, place in vacation.items():
    print(person.title() + ' would love to travel to ' + place.title() + ', at least once in their life.')