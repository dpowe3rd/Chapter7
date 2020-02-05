prompt = 'How many guests are in your party today?\n'

guests = input(prompt)
guests = int(guests)

if guests >= 8:
    print('\nI\'m sorry but you have ' + str(guests) + ' guests in  your party, I must ask you to wait for a table.')

else:
    print('\nWill all ' + str(guests) + ' of you please follow me, your table is this way.')
