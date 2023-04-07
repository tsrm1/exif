import os
from exif import Image

new_jpg_folder = "JPG"
path = os.getcwd()  # определение текущей директории

file_type = '.jpg'

# получаем список файлов, удовлетворяющих критерию
with os.scandir(path) as files:
    files = [file.name for file in files if file.is_file() and file.name.endswith(file_type)]



def create_folder(new_jpg_folder):
    try:
        os.mkdir(new_jpg_folder)
    except IOError as error:
        print(error)

create_folder(new_jpg_folder)

for file in files:
    with open(file, 'rb') as img_file:
        image = Image(img_file)
        if image.has_exif:
            img_orientation = image.get('orientation')
            image.delete_all()
            image.orientation = img_orientation
            with open(new_jpg_folder + '/' + file, 'wb') as new_file:
                new_file.write(image.get_file())
                print(file, '- EXIF deleted.')
        else:
            print(f"Image {file} does not contain any EXIF information.")


