#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Image2Icon
# @raycast.mode silent

# Optional parameters:
# @raycast.icon 🤖
# @raycast.argument1 { "type": "text", "placeholder": "Placeholder" }
# @raycast.packageName Quick Tools

# Documentation:
# @raycast.author SecNex
# @raycast.authorURL https://docs.secnex.io

import os
import sys
from PIL import Image

print("Image2Icon - Convert images to ICO files")

def convert_to_ico(input_file, output_file):
    try:
        img = Image.open(input_file)
        img.save(output_file, format='ICO')
        print(f"Converted {input_file} to {output_file} successfully.")
    except Exception as e:
        print(f"Failed to convert {input_file}: {e}")

def convert_images_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            input_path = os.path.join(directory, filename)
            output_path = os.path.join(directory, os.path.splitext(filename)[0] + '.ico')
            convert_to_ico(input_path, output_path)

def process_path(path):
    if os.path.isdir(path):
        print(f"Processing directory: {path}")
        convert_images_in_directory(path)
    elif os.path.isfile(path):
        print(f"Processing single file: {path}")
        output_path = os.path.splitext(path)[0] + '.ico'
        convert_to_ico(path, output_path)
    else:
        print(f"The path {path} is neither a file nor a directory.")

if __name__ == "__main__":
    path = sys.argv[1]
    try:
        process_path(path=path)
    except Exception as e:
        print(f"Failed to convert {path}: {e}")
        sys.exit(1)


