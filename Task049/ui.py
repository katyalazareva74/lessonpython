from logger import print_data, input_data, find_data, changes_data

def interface():
    print("""Выберете режим работы:
            1 - запись данных
            2 - вывод данных
            3 - поиск данных
            4 - удаление данных
            5 - изменение данных
              """)
    command = int(input('Введите номер команды: '))
    while command < 1 or command > 5:
        command = int(input('Введите корректный номер команды: '))
    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        print('Введите параметры поиска данных через ; ')
        filter_string = (input()).lower()
        find_data(filter_string)
    elif command == 4:
        print('Введите параметры удаления данных через ; ')
        filter_string = (input()).lower()
        changes_data(filter_string, '')
    elif command == 5:
        print('Введите параметры, требующие изменения ; ')
        filter_string = (input()).lower()
        print('Введите новые данные ; ')
        changes_string = (input())
        changes_data(filter_string, changes_string)