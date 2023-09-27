import os
import xml.etree.ElementTree as ET


def update_svg_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.svg'):
            file_path = os.path.join(directory, filename)
            tree = ET.parse(file_path)
            root = tree.getroot()

            # Find all elements with the 'fill' attribute and update their value
            for elem in root.iter():
                fill_attr = elem.get('fill')
                if fill_attr is not None:
                    elem.set('fill', '#0B2545')

            # Create a new filename with the suffix '.white.svg'
            new_filename = os.path.splitext(filename)[0] + '.blue.svg'
            new_file_path = os.path.join(directory, new_filename)

            # Save the modified SVG content to the new file
            tree.write(new_file_path)

            print(f'Successfully updated and saved: {new_filename}')


# Specify the directory containing the SVG files
directory_path = "D:\Projects\Contract Projects\Arz X - Pay Libero\Source Codes\paylibero\public\icons"

# Call the function to update SVG files
update_svg_files(directory_path)
