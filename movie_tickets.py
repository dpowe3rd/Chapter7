prompt = 'Welcome to our movie theatre, please tell me how old you are so I can accurately price your ticket.\n'
active = True

while active:
    age = input(prompt)
    age = int(age)

    if age < 3:
        print('Well little one, since you\'re only ' + str(age) + ' years old your ticket is free!')
        break
    elif 3 <= age < 12:
        print('Hello young person, since you\'re ' + str(age) + ' years old your ticket is $10')
        break
    else:
        print('Hello, since you\'re ' + str(age) + ', your ticket is $15')
        break
