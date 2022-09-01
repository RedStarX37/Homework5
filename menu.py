from file_manager import create_folder, delete_folder, copy_file_folder, view_directory, view_only_folders, \
    view_only_files, view_os_info, view_creator

from victory import game
from bank_account import bank


def menu_bar():
    print('МЕНЮ\n1.  создать папку;\n2.  удалить (файл/папку);\n3.  копировать (файл/папку);'
          '\n4.  просмотр содержимого рабочей директории;\n5.  посмотреть только папки;\n6.  посмотреть только файлы;'
          '\n7.  просмотр информации об операционной системе;\n8.  создатель программы;\n9.  играть в викторину;'
          '\n10. мой банковский счет;\n11. выход.\n')

    selection = input('Выберите один из пунктов: ')
    return selection


def get_selection():
    selection = menu_bar()

    if selection == '1':
        create_folder()
    elif selection == '2':
        delete_folder()
    elif selection == '3':
        copy_file_folder()
    elif selection == '4':
        view_directory()
    elif selection == '5':
        view_only_folders()
    elif selection == '6':
        view_only_files()
    elif selection == '7':
        view_os_info()
    elif selection == '8':
        view_creator()
    elif selection == '9':
        game()
        print('\n')
    elif selection == '10':
        bank()
    elif selection == '11':
        exit()
    else:
        get_selection()

    get_selection()


get_selection()
