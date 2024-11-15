#Сортируем файлы из папки S:\\Изучение English, которые были добавлены в течение суток
import os
import time

lst = []

for address, dirs, files in os.walk ('S:\\Изучение English'):
    for file in files:
        full = os.path.join(address, file)
        if time.time() - os.path.getctime(full) < 86400:
            lst.append(full)

for c, value in enumerate (lst, 1):
    print (c, value)

