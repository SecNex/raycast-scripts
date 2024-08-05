#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title PDF2Image
# @raycast.mode silent

# Optional parameters:
# @raycast.icon 📄
# @raycast.argument1 { "type": "text", "placeholder": "Path to PDF" }
# @raycast.packageName Quick Tools

# Documentation:
# @raycast.author SecNex
# @raycast.authorURL https://docs.secnex.io

import os
import sys
import pdf2image as pdf2img

print("PDF2Image - Convert PDF files to images")

def convert_pdf_to_image(input_file, output_folder):
    try:
        # Convert PDF to a list of PIL images
        images = pdf2img.convert_from_path(input_file)
        
        # Save each page as an image
        for i, image in enumerate(images):
            output_file = os.path.join(output_folder, f"{os.path.splitext(os.path.basename(input_file))[0]}_page_{i + 1}.png")
            image.save(output_file, 'PNG')
            print(f"Saved {output_file} successfully.")
    except Exception as e:
        print(f"Failed to convert {input_file}: {e}")

def process_path(path):
    if os.path.isfile(path) and path.lower().endswith('.pdf'):
        print(f"Processing single file: {path}")
        output_folder = os.path.dirname(path)
        convert_pdf_to_image(path, output_folder)
    else:
        print(f"The path {path} is not a valid PDF file.")

if __name__ == "__main__":
    path = sys.argv[1]
    try:
        process_path(path=path)
    except Exception as e:
        print(f"Failed to convert {path}: {e}")
        sys.exit(1)