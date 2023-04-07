import os

# определение текущей рабочей директории
# path = os.getcwd()

# path = "./images/"
path = "."

# чтение записей
with os.scandir(path) as listOfEntries:
    for entry in listOfEntries:
        # печать всех записей, являющихся файлами
        if entry.is_file():
            print(entry.name)


print()
print('Только файлы')
with os.scandir(path) as files:
    files = [file.name for file in files if file.is_file()]
print(files)

print()
print('Только папки')
with os.scandir(path) as files:
    files = [file.name for file in files if file.is_dir()]
print(files)

print()
print('Только файлы *.py')
with os.scandir(path) as files:
    files = [file.name for file in files if file.is_file() and file.name.endswith('.py')]
print(files)

print()
# Список подкаталогов каталога с помощью scandir
print('Только папки')
with os.scandir(path) as files:
    subdir = [file.name for file in files if file.is_dir()]
print(subdir)

