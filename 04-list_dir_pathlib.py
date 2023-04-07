import pathlib

images_folder = "./images/"
current_folder = "."

# определение пути
currentDirectory = pathlib.Path(images_folder)

# определение шаблона
currentPattern = "*.jpg"

# Вариант 1
for currentFile in currentDirectory.iterdir():
    print(currentFile)

print()

# Вариант 2, с применением шаблона
for currentFile in currentDirectory.glob(currentPattern):
    print(currentFile)

print()
print('Только папки')
dir = pathlib.Path(current_folder)
files = [file.name for file in dir.iterdir() if file.is_dir()]