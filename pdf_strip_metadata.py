#! /usr/bin/env python3
# This script will strip metadata from all PDF files in a directory and save them to a new directory.

import os
import PyPDF2

def display_metadata(reader):
    """Display metadata of the PDF file."""
    metadata = reader.metadata
    print("Metadata:")
    for key, value in metadata.items():
        print(f"{key}: {value}")

def strip_metadata_from_directory(directory_path, output_directory):
    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Loop through all files in the directory
    for filename in os.listdir(directory_path):
        if filename.lower().endswith('.pdf'):
            input_pdf_path = os.path.join(directory_path, filename)
            output_pdf_path = os.path.join(output_directory, filename)

            # Open the input PDF file
            with open(input_pdf_path, 'rb') as input_pdf_file:
                reader = PyPDF2.PdfReader(input_pdf_file)
                writer = PyPDF2.PdfWriter()

                # Display metadata
                print(f"\nProcessing file: {filename}")
                display_metadata(reader)
                
                # Copy all pages from the reader to the writer
                for page_num in range(len(reader.pages)):
                    writer.add_page(reader.pages[page_num])

                # Remove metadata
                writer._info = PyPDF2.generic.DictionaryObject()

                # Write the output PDF file
                with open(output_pdf_path, 'wb') as output_pdf_file:
                    writer.write(output_pdf_file)

# Define the directory paths
home_directory = os.path.expanduser('~')
directory_path = os.path.join(home_directory, 'Documents', 'original_pdf')
output_directory = os.path.join(home_directory, 'Documents', 'output_pdf')

# Identify whether the directory_path exists
if not os.path.exists(directory_path):
    print(f"Directory {directory_path} does not exist.  Creating it now.")
    # create the directory_path
    os.makedirs(directory_path, exist_ok=True)

# Identify whether the output_directory exists
if not os.path.exists(output_directory):
    print(f"Directory {output_directory} does not exist.  Creating it now.")
    # create the output_directory
    os.makedirs(output_directory, exist_ok=True)

# Identify whether there are any PDF files in the directory_path
if not os.listdir(directory_path):
    print(f"Directory {directory_path} does not contain any PDF files.  Please put some PDF files in this directory and try again.")
else:
    #launch the strip_metadata_from_directory function if any pdf files are present
    strip_metadata_from_directory(directory_path, output_directory)