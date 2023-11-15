from data_create import name_data, surname_data, phone_data, address_data

# все элементы внтутри строки разделены символом |
def save_first(data_first):
    with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
        for item in data_first:
            item_splitted = item.split('|')
            val = "{0}\n{1}\n{2}\n{3}\n\n".format(
                item_splitted[0], item_splitted[1], item_splitted[2], item_splitted[3])
            file.write(val)


def read_first():
    data_first_version_second = []
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        val = ""
        for line in file.readlines():
            if line == '\n':
                if len(val) is not 0:
                    data_first_version_second.append(val)
                val = ""
                continue
            if len(val) is not 0:
                val += "|"
            val += line.strip()
        if len(val) is not 0:
            data_first_version_second.append(val)
    return data_first_version_second

def input_data():
    data_first, data_second = print_data()
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int (input (f"В каком формате вы хотите записать данные?\n\n"
                      f"1 Вариант:\n\n"
                      f"{surname}\n"
                      f"{name}\n"
                      f"{phone}\n"
                      f"{address}\n\n"
                      f"2 Вариант:\n\n"
                      f"{surname}; {name}; {phone}; {address}\n\n"
                      f"Выберите номер варианта: "))
    
    while var not in {1, 2}:
        print ('Вы ввели неверный номер')
        var = int(input("Введите номер варианта: "))

    if var == 1:
        data_first.append(f'{name}|{surname}|{phone}|{address}')
        save_first(data_first)
    else:
        with open ('data_second_variant.csv', 'a', encoding = 'utf-8') as file:
            file.write (f'{name};{surname};{phone};{address}\n')

def print_data():
        data_first_version_second = []
        print ('Вывод данных из 1-го файла\n')
        data_first = read_first()
        for item in data_first:
            item = item.split('|')
            print('\n'.join(item))
            print('\n')
        print ('Вывод данных из 2-го файла\n')
        with open ('data_second_variant.csv', 'r', encoding = 'utf-8') as file:
            data_second = list (file.readlines())
            print (*data_second)
        return data_first, data_second
    
def put_data():
    print ('Из какого файла Вы хотите изменить данные?')
    data_first, data_second = print_data()
    number_file = int (input ('Введите номер файла: '))

    while number_file !=1 and number_file !=2:
        print ('Вы ввели неверный номер файла')
        number_file = int (input ('Введите номер файла: '))

    if number_file == 1:
        print ("Какую запись по счету Вы хотите изменить?")
        number_journal = int (input ('Введите номер записи: '))
        number_journal -= 1
        print (f'Изменить данную запись\n{data_first[number_journal]}')
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = address_data()
        data_first = data_first[:number_journal] + [f'{name}|{surname}|{phone}|{address}'] + \
                     data_first[number_journal+ 1:]
        save_first(data_first)
        print('Изменения успешно сохранены!')
    else:
        print("Какую запись по счету Вы хотите изменить?")
        number_journal = int (input ('Введите номер записи: '))
        number_journal -=1
        print (f'Изменить данную запись\n{data_second[number_journal]}')
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = address_data()
        data_second = data_second[:number_journal] + [f'{name}; {surname}; {phone}; {address}\n'] + \
                      data_second[number_journal+1:]
        with open ('data_second_variant.csv', 'w', encoding = 'utf-8') as file:
           file.write(''.join(data_second))
        print('Изменения успешно сохранены!')

def delete_data():
    print ("Из какого файла Вы хотите удалить данные?")
    data_first, data_second = print_data()
    number_file = int (input ('Введите номер файла: '))

    while number_file not in {1, 2}:
        number_file = int (input ('Введите номер файла: '))
        if number_file not in {1, 2}:
            print('Вы ввели неверный номер файла')

    if number_file == 1:
        print ("Какую запись по номеру Вы хотите удалить?")
        number_journal = -1

        while number_journal < 1:
            number_journal = int (input ('Введите номер записи (1..x) -1 для выхода: '))
            if number_journal is -1: return

        print (f'Удалить данную запись\n{data_first[number_journal-1]}')
        data_first.pop(number_journal-1)
        save_first(data_first)
        print('Изменения успешно сохранены!')
    else:
        print("Какую запись по счету Вы хотите удалить?")
        number_journal = int (input ('Введите номер записи: '))
        print (f'Удалить данную запись\n{data_second[number_journal-1]}')
        data_second = data_second[:number_journal] + data_second[number_journal+1:]
        with open ('data_second_variant.csv', 'w', encoding = 'utf = 8') as file:
           file.write(''.join(data_second))
        print('Изменения успешно сохранены!')        