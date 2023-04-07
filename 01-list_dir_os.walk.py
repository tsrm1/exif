import os

images_folder = "./images/"
current_folder = "."

# перечень всех каталогов и файлов в текущем "." каталоге. Используем os.walk()
for root, dirs, files in os.walk(current_folder):
    for filename in files:
        print(filename)


