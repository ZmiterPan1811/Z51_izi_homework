import os

# Переменные
name_book = str(input())    # запрос
book_case = r'C:\projects\for_git\books'    # путь к папке с файлами txt
files_list = os.listdir(book_case)      # список названий файлов (книг) в исходном виде
ru_books_name = []      # список названий книг на русском (из содержания файлов)
books_on_demand = {}    # словарь, содержащий совпадения по запросу

''' Функция находит в открытом и считываемом файле название книги
на русском языке и добавляет в отдельный список русских названий "ru_books_name". 
Название отделено от автора '\n\n'.
Cрез от '\n\n' до следующего '\n' и есть искомое название книги. '''
def extract_ru_title_book(reading_file):
    count = 0
    for j in range(len(reading_file)):
        if reading_file[j] == '\n':
            count += 1
        if count == 3:
            b = j
            break
    c = reading_file.find('\n\n')
    ru_books_name.append(reading_file[c:b].replace('\n', '', 2))

''' Функция формирует словарь с совпадениями "books_on_demand" 
(название оригинального файла: название книги на русском)'''
def parsing_result(ru_books_name):
    for i in range(len(ru_books_name)):
        if name_book.lower() in ru_books_name[i].lower():
            books_on_demand[files_list[i]] = ru_books_name[i]
    return books_on_demand

''' Основной процесс. Часть файлов в UTF-8, часть нет. 
Если применить encoding='utf-8' ко всем файлам, программа ругается.
Мозгов не хватило, сделал так.'''
for i in range(len(files_list)):    # перебираем каждое название текстового файла по его индексу в списке
    try:
        file = open(f'books\{files_list[i]}', 'r')      # открываем файл. путь указан
        reading_file = file.read()      # читаем файл
        extract_ru_title_book(reading_file)     # вызываем функцию для нахождения названия книги на русском
        file.close()        # закрываем файл
    except:
        file = open(f'books\{files_list[i]}', 'r', encoding='utf-8')    # если файл не в 'utf-8', декодируем
        reading_file = file.read()
        extract_ru_title_book(reading_file)
        file.close()

parsing_result(ru_books_name)   # вызываем функцию, составляющюю словарь совпадений

for key, value in books_on_demand.items():
    print(f'Текстовый файл - {key}. Название книги - {value}.')
'''
Работает, правда, на поиск совпадения-строки. Не выделил времени расписать, 
чтобы производило поиск совпадений слов из списка "запроса" в списке слов "названия".  
'''




