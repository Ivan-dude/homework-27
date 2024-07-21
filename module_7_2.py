def custom_write(file_name, info):
    dict_ = {}
    file = open(file_name, 'w', encoding='utf-8') #открываем фаил для записи
    for i in range(len(info)):
        dict_[(i + 1, file.tell())] = info[i]
        file.write(info[i] + '\n') #записываем строки
    file.close()
    return dict_ #выводим словарь

file_name = 'test.txt'
info = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!']
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
