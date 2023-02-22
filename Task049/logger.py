import os
from data_create import name_data, surname_data, phon_data, adress_data

file_name =  'data.txt'

def print_data():
    print('Вывод данных из файла: ')
    with open(file_name, 'r', encoding='utf-8') as file:
       data_list = file.readlines()
       for element in data_list:
           print(element)

def input_data():
    print('Введите данные для записи в файл: ')
    name = name_data()
    surname = surname_data()
    phon = phon_data()
    adress = adress_data()
    with open(file_name, 'a', encoding='utf-8') as file:
        file.writelines(f"{name};{surname};{phon};{adress};\n")

def find_data(filter_str):
    if ';' in filter_str:
        list_filter = filter_str.split(';')
    else:
        list_filter = [filter_str]
    is_found = False
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            data_list = file.readlines()
            for elem in data_list:
                count = 0
                temp_record = elem.split(';')
                for record in temp_record:
                    for el_filter in list_filter:
                        if (el_filter in record.lower()) and (len(record)==len(el_filter)):
                            count +=1
                if count == len(list_filter):
                    is_found = True
                    print(elem)
            if not is_found:
                print('Записей не найдено')
    else:
        print('Файл не существует, записей нет.')

def changes_data(filter_str, changes_str):
    if ';' in filter_str:
        list_filter = filter_str.split(';')
    else:
        list_filter = [filter_str]
    is_found = False
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            data_list = file.readlines()
            res_list = list()
            for elem in data_list:
                temp_record = elem.split(';')
                temp_rec1 = str()
                for record in temp_record:
                    for el_filter in list_filter:
                        if (el_filter in record.lower()) and (len(record)==len(el_filter)):
                            record = record.replace(record, changes_str)
                            is_found = True
                    if record == '\n':
                        temp_rec1+= '\n'
                    elif (record != '\n') and (record != ''):
                        temp_rec1+= record+';'
                if temp_rec1 != '\n':
                    res_list.append(temp_rec1)
            record_data(res_list)
            if not is_found:
                print('Записей не найдено')
    else:
        print('Файл не существует, записей нет.')

def record_data(result):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.writelines(result)