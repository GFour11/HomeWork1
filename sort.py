import sys
import defs
import os


path = sys.argv[1]                                                   # Цикл запитує шлях до папки, яку потрібно відсортувати
if os.path.isdir(path):
    create_new_dirs= defs.create_dirs(path)                          #Створюємо нові папки, куди будемо сортувати файли
    first_sort=defs.sort_files(defs.get_file_paths(path), path)      #Сортуємо файли в першочеговій папці
    second_sort = defs.full_sort(path)                               #Сортуємо файли в усіх інших папках, незважаючи на глибину вкладення
    archives_unpacker= defs.dearchivator(path)                       #Розпаковуємо архіви
    clean=defs.folder_remover(path)                                  #Видаляємо порожні папки
    result_file=defs.annotation_file(path)                           #Вертаємо ТХТ файл зі змістом відсортованої папки
    print('Ваші файли відсортовано')
else:
    print("Шлях до папки вказано не вірно")



