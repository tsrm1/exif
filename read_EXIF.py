import os
from exif import Image

path_from = "./images/"
new_jpg_folder = "JPG"
# path = os.getcwd()  # определение текущей директории

file_type = '.jpg'

def get_image_member(image):
    return dir(image)


def dms_coordinates_to_dd_coordinates(coordinates, coordinates_ref):
    decimal_degrees = coordinates[0] + \
                      coordinates[1] / 60 + \
                      coordinates[2] / 3600

    if coordinates_ref == "S" or coordinates_ref == "W":
        decimal_degrees = -decimal_degrees

    return round(decimal_degrees, 7)

def get_gps(image):
    try:
        print(f"GPS: Latitude: {dms_coordinates_to_dd_coordinates(image.gps_latitude, image.gps_latitude_ref)}")
        print(f"GPS: Longitude: {dms_coordinates_to_dd_coordinates(image.gps_longitude, image.gps_longitude_ref)}")
        print(f"http://maps.google.com/maps?t=h&q={dms_coordinates_to_dd_coordinates(image.gps_latitude, image.gps_latitude_ref)},{dms_coordinates_to_dd_coordinates(image.gps_longitude, image.gps_longitude_ref)}")
    except AttributeError as error:
        print(f"GPS: Unknown")

# получаем список файлов, удовлетворяющих критерию
with os.scandir(path_from) as files:
    files = [file.name for file in files if file.is_file() and file.name.endswith(file_type)]
# print(files)


def create_folder(new_jpg_folder):
    try:
        os.mkdir(new_jpg_folder)
    except IOError as error:
        print(error)

create_folder(new_jpg_folder)

for file in files:
    with open(path_from + file, 'rb') as img_file:
        image = Image(img_file)
        if image.has_exif:
            print(f"Image {file} contains EXIF (version {image.exif_version}) information.")
            # print(get_image_member(image))
            print(f'Make: {image.make}, Model: {image.model}')
            print(f"Lens make: {image.get('lens_make', 'Unknown')}")
            print(f"Lens model: {image.get('lens_model', 'Unknown')}")
            print(f"Lens specification: {image.get('lens_specification', 'Unknown')}")
            print(f"OS version: {image.get('software', 'Unknown')}")
            if image.get('software', 'None') != 'None':
                image.delete('software')
                print(f"OS version: {image.get('software', 'Unknown')} - Deleted!")

            print(f"Time original: {image.datetime_original}.{image.subsec_time_original} UTC: {image.get('offset_time', '')}")
            get_gps(image)

            new_file_name = new_jpg_folder + '/IMG_'
            for char in str(image.datetime_original):
                if char != ":":
                    if char == ' ':
                        new_file_name += '_'
                    else:
                        new_file_name += char
            new_file_name += '.' + image.subsec_time_original + '_' + image.make + '.jpg'
            # print(dir(image))
            # print(image.get_all())
            # перезапись файла с новым названием
            with open('./' + new_file_name, 'wb') as new_file:
                new_file.write(image.get_file())
                print(new_file_name, ' - saved.')
            print()
        else:
            print(f"Image {file} does not contain any EXIF information.")


