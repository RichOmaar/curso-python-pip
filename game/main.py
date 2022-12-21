import random

options = ['piedra', 'papel', 'tijera']
computer_wins = 0
user_wins = 0
round = 1

while True:
    print('*' * 10)
    print('ROUND', round)
    print('*' * 10)
    print('CPU =>', computer_wins)
    print('Usuario =>', user_wins)

    user_option = input('piedra, papel o tijera: ').lower()
    if not user_option in options:
        print('La opción seleccionada no es valida')
        continue
    computer_option = random.choice(options)

    print('User option =>', user_option)
    print('Computer option =>', computer_option)

    if user_option == computer_option:
        print('Empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('piedra gana a tijera')
            print('Ganó el usuario!')
            user_wins += 1
        else:
            print('papel gana a piedra')
            print('Ganó el CPU!')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'tijera':
            print('tijera gana a papel')
            print('Ganó el CPU!')
            computer_wins += 1
        else:
            print('papel gana a piedra')
            print('Ganó el usuario!')
            user_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')
            print('Ganó el usuario!')
            user_wins += 1
        else:
            print('piedra gana a tijera')
            print('Ganó el CPU!')
            computer_wins += 1

    round += 1

    if computer_wins == 2:
        print('El aganador es el CPU')
        break
    if user_wins == 2:
        print('El aganador es el usuario')
        break
