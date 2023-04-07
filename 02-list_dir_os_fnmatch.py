import os, fnmatch

images_folder = "./images/"
current_folder = "."

# перечень всех каталогов и файлов в текущем "." каталоге. Используем os.walk()
listOfFiles = os.listdir(images_folder)
pattern = "*.jpg"
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
        print(entry)

