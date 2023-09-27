import os
import pyheif
from PIL import Image

# Input directory containing HEIC files
input_directory = "/mnt/d/Data/Digital Information/Memories - Images - Videos/Ayhan/02 - Infant"

# Output directory for saving JPEG files
output_directory = "/mnt/d/convert/jpg"

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Get a list of all HEIC files in the input directory
heic_files = [f for f in os.listdir(input_directory) if f.endswith(".heic")]

# Iterate through each HEIC file and convert it to JPEG
for heic_file in heic_files:
    heic_path = os.path.join(input_directory, heic_file)
    output_path = os.path.join(output_directory, os.path.splitext(heic_file)[0] + ".jpg")

    # Open the HEIC image using pyheif
    heif_file = pyheif.read(heic_path)
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )

    # Save it as JPEG
    image.save(output_path, "JPEG")

    print(f"Converted {heic_path} to {output_path}")

print("Conversion complete.")

