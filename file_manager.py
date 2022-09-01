import os
import sys
import shutil
import socket


def create_folder():
    print('Создание новой папки\n')
    new_folder_name = input('Придумайте название новой папки: ')
    os.mkdir(f'{new_folder_name}')


def delete_folder():
    print('Удаление папки\n')
    del_folder_name = input('Название удаляемой папки: ')
    os.rmdir(f'{del_folder_name}')


def copy_file_folder():
    print('Копирование папки/файлв\n')
    unit_name = input('Название папки/файла: ')
    copy_loc = input('Место копирования: ')
    loc = f'{unit_name}'
    dest = f'{copy_loc}'
    shutil.copyfile(loc, dest)


def view_directory():
    print('Viewing directory\n')
    print(os.listdir())


def view_only_folders():
    print('Просмотр папок\n')
    folders = [f for f in os.listdir('.') if os.path.isdir(f)]
    print(folders)


def view_only_files():
    print('Просмотр файлов\n')
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    print(files)


def view_os_info():
    print('Операционная система: '+ sys.platform + '\n')


def view_creator():
    print('Создатель программы: ' + socket.gethostname() + '\n')