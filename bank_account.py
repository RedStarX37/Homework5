def bank():
    balance = 0

    def bank_menu():
        print('\nБаланс: ' + str(balance))
        print('\nМЕНЮ\n1. пополнить счёт;\n2. снять деньги;\n3. выход.\n')
        choice = input('Выберите один из пунктов: ')
        return choice

    loop = 1
    while loop == 1:

        choice = bank_menu()

        if choice == '1':
            adding = int(input('Сумма пополнения: '))
            balance = balance + adding
            print('Баланс пополнен на ' + str(adding) + '\n')

        elif choice == '2':
            withdrawal = int(input('Сумма снятия: '))

            if withdrawal <= balance:
                balance -= withdrawal
            print('С счёта были сняты ' + str(withdrawal) + '\n')

        elif choice == '3':
            print('\n')
            break
