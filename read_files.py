import os


def list_files(directory):
    file_names = []
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_names.append(os.path.splitext(filename)[0])
    return file_names


def write_file_names(directory, output_file):
    file_names = list_files(directory)
    with open(output_file, 'w') as file:
        for filename in file_names:
            file.write(f"<IconItem name=\"{filename}\">\n")
            file.write(f"   <IconExample name=\"{filename}\"/>\n")
            file.write(f"</IconItem>\n")


# Replace 'directory_path' with the path to your desired directory
directory_path = 'D:/Projects/Contract Projects/Arz X - Pay Libero/Source Codes/paylibero/public/icons'


# Replace 'output_file_path' with the desired path and name for the output file
output_file_path = 'D:/Projects/Contract Projects/Arz X - Pay Libero/Source Codes/paylibero/components/atoms/Icon/file_names.js'

write_file_names(directory_path, output_file_path)
