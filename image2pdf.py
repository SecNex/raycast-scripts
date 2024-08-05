#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Image2PDF
# @raycast.mode silent

# Optional parameters:
# @raycast.icon 🖼️
# @raycast.argument1 { "type": "text", "placeholder": "Path to image" }
# @raycast.packageName Quick Tools

# Documentation:
# @raycast.author SecNex
# @raycast.authorURL https://docs.secnex.io

import os
import sys
from PIL import Image

print("Image2PDF - Convert images to PDF files")

def convert_image_to_pdf(input_file, output_file):
    try:
        img = Image.open(input_file)
        pdf_path = os.path.splitext(output_file)[0] + '.pdf'
        img.save(pdf_path, 'PDF', resolution=100.0)
        print(f"Converted {input_file} to {pdf_path} successfully.")
    except Exception as e:
        print(f"Failed to convert {input_file}: {e}")

def process_path(path):
    if os.path.isfile(path) and path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        print(f"Processing single file: {path}")
        output_path = os.path.splitext(path)[0] + '.pdf'
        convert_image_to_pdf(path, output_path)
    else:
        print(f"The path {path} is not a valid image file.")

if __name__ == "__main__":
    path = sys.argv[1]
    try:
        process_path(path=path)
    except Exception as e:
        print(f"Failed to convert {path}: {e}")
        sys.exit(1)