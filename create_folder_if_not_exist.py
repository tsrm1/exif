import os

folder_name = input("Enter folder name:")

dir_name = '_'.join(i for i in folder_name.split(" ") if i.isalnum())   # формируем имя папки, удаляя пробелы и спецсимволы
print(dir_name)

if not os.path.exists((dir_name)):      # создаём папку, если её нет
    os.makedirs(dir_name)