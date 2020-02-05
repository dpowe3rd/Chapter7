prompt = "Please enter the pizza toppings you would like. Enter 'quit' if you would like to stop."
on = True

print(prompt)

while on:
    toppings = input()
    print('Okay, I am adding ' + toppings + ' to your pizza.')

    if toppings == 'quit':
        print('I\'m done putting toppings on your pizza.')
        break
