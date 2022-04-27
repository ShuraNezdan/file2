def list_creation():
    # Создаем словарь первичный
    list_union = [
        {'File name': '1.txt', 'number of lines' : 0},
        {'File name': '2.txt', 'number of lines' : 0},
        {'File name': '3.txt', 'number of lines' : 0}    
    ]
    
    # Подсчитываем и вводим в словарь колличество строк в файле
    for i in list_union:
        number_of_lines = sum(1 for line in open(i['File name'], 'r'))
        i['number of lines'] = number_of_lines
        
    return list_union

def write_to_file():

    counter = []  # Индексы
    index_max = [] # Содержит колличество строк в файлах
    counter_file = 1  # Счетчик файлов

    # Создаем список из number of lines(колличества строк в файле) и создаем переменню из отсортированных значений
    for i in list_creation():
        index_max.append(i["number of lines"])
    sort_index = sorted(index_max)

    # Создаем список индексов от number of lines(колличества строк в файле)
    for i in sort_index:
        counter.append(index_max.index(i))


    # Перебераем индексы и работаем от них
    for y in counter:
        
        # Считываем из файла нформацию
        with open(list_creation()[y]['File name']) as f:
            data = f.read()
            # Записываем и добавляем в новый файл информацию по условию
            # True создает фойл и записывает, Else добавляет в ранее созданный
            if counter_file == 1:
                with open('data.txt', 'w') as f_wr:
                    name_file = list_creation()[y]['File name']
                    f_wr.write(f'{name_file}\n{counter_file}\n{data} \n')
                counter_file += 1
            else:
                with open('data.txt', 'a') as f_wr:
                    name_file = list_creation()[y]['File name']
                    f_wr.write(f'{name_file}\n{counter_file}\n{data} \n')
                counter_file += 1
    return

write_to_file()