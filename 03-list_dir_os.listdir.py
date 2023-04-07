import os

images_folder = "./images/"
current_folder = "."

# Вариант 1
def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

for file in files(current_folder):
    print(file)



print()

# Вариант 2. Файлы и папки
def directory(path):
    for file in os.listdir(path):
        print(file)

directory(current_folder)

print()

# Вариант 3. Файлы и папки
with os.scandir(current_folder) as files:
    for file in files:
        print(file.name)

print()

# Вариант 4. Файлы, удовлетворяющие критерию
content = os.listdir(images_folder)
images = []
for file in content:
    if os.path.isfile(os.path.join(images_folder, file)) and file.endswith('.jpg'):
        images.append(file)
print(images)

