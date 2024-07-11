def custom_write(file_name, info):
    file1 = open(file_name, 'w') #открываем фаил для записи
    tell_1_pos = file1.tell() #узнаем номера байта начала строки
    file1.write(f'{info[0]}\n') #записываем первую строку
    tell_2_pos = file1.tell()
    file1 = open(file_name, 'a', encoding='utf-8')
    file1.write(f'{info[1]}\n') #записываем след. строку
    tell_3_pos = file1.tell()
    file1.write(f'{info[2]}\n') #записываем след. строку
    tell_4_pos = file1.tell()
    file1.write(f'{info[3]}') #записываем след. строку
    file1 = open(file_name, 'r', encoding='utf-8')
    # for index, line in enumerate(file1, 1): #попробовал получить номера строк
    #     print(index)
    file1.close()
    keys = [(1, tell_1_pos), (2, tell_2_pos), (3, tell_3_pos), (4, tell_4_pos)] #создал для удобства
    strings_position = dict(zip(keys, info)) #собираем всё в словарь
    return strings_position #выводим получившийся словарь
file_name = 'test.txt'
info = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!']
result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)






