
def game():

    import random
    questions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    variant = random.sample(questions, 5)
    variant.sort()

    score = 0

    for question in variant:
        if 1 in variant:
            answer = input('Год рождения Максима Галкина: ')
            # 18.06.1976
            if answer == '18.06.1976':
                score = score + 1
            else:
                score = score
        else:
            pass

        if 2 in variant:
            answer = input('Год рождения Аллы Пугачёвой: ')
            # 15.04.1949
            if answer == '15.04.1949':
                score = score + 1
            else:
                score = score
        else:
            pass

        if 3 in variant:
            answer = input('Год рождения Филиппа Киркорова: ')
            # 30.04.1967
            if answer == '30.04.1967':
                score = score + 1
            else:
                score = score
        else:
            pass

        if 4 in variant:
            answer = input('Год рождения Сергея Зверева: ')
            # 1963
            if answer == '19.07.1963':
                score = score + 1
            else:
                score = score
        else:
            pass

        if 5 in variant:
            answer = input('Год рождения Бориса Моисеева: ')
            # 04.03.1954
            if answer == '04.03.1954':
                score = score + 1
            else:
                score = score
        else:
            pass

        if 6 in variant:
            answer = input('Год рождения Земфиры: ')
            # 26.08.1976
            if answer == '26.08.1976':
                score = score + 1
            else:
                score = score
        else:
            pass

        if 7 in variant:
            answer = input('Год рождения Дианы Арбениной: ')
            # 08.07.1974
            if answer == '08.07.1974':
                score = score + 1
            else:
                score = score
        else:
            pass

        if 8 in variant:
            answer = input('Год рождения Глюкозы: ')
            # 07.06.1986
            if answer == '07.06.1986':
                score = score + 1
            else:
                score = score
        else:
            pass

        if 9 in variant:
            answer = input('Год рождения Сергея Шнурова: ')
            # 13.04.1973
            if answer == '13.04.1973':
                score = score + 1
            else:
                score = score
        else:
            pass

        if 10 in variant:
            answer = input('Год рождения Игоря Крутого: ')
            # 29.07.1954
            if answer == '29.07.1954':
                score = score + 1
            else:
                score = score
        else:
            pass

        wrongs = 5 - score
        correctpercent = score * 100 / 5
        wrongpercent = 100 - correctpercent

        print('Количество правильных ответов:', score)
        print('Количество неправильных ответов:', wrongs)
        print('Процент правильных ответов:', correctpercent)
        print('Процент неправильных ответов:', wrongpercent)

        proceed = input('Вы хотите начать игру сначала? (да/нет): ')
        if proceed == 'нет':
            break
