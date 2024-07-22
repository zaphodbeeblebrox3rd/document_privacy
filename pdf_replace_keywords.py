#! /usr/bin/env python3
# This script will replace keywords in a PDF file with the value of a variable.
# Keywords in the document as well as keywords in the document metadata are replaced
# The output is saved to a new file.

import os
import shutil
import fitz  # PyMuPDF
import PyPDF2

# Define the directory paths
home_directory = os.path.expanduser('~')
directory_path = os.path.join(home_directory, 'Documents', 'original_pdf')
output_directory = os.path.join(home_directory, 'Documents', 'output_pdf')
temp_directory = os.path.join(home_directory, 'Documents', 'temp_pdf')

# Define the path to custom font files
custom_fonts = {
    "helv": "/path/to/Helvetica.ttf",
    "times": "/path/to/TimesNewRoman.ttf",
    # Add more fonts as needed
}

# Prompt user for keywords to replace and the replacement values
keyword_to_replace = input("Enter the keyword to replace: ")
replacement_value = input("Enter the replacement value: ")

def replace_text_in_pdf(input_pdf_path, output_pdf_path, keyword, replacement):
    # Open the input PDF
    pdf_document = fitz.open(input_pdf_path)
    
    # Iterate through each page
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text_instances = page.search_for(keyword)
        
        # Replace each instance of the keyword
        for inst in text_instances:
            # Get the font and size of the original text
            text = page.get_text("dict", clip=inst)
            if text["blocks"]:
                block = text["blocks"][0]
                if block["lines"]:
                    line = block["lines"][0]
                    if line["spans"]:
                        span = line["spans"][0]
                        font_name = span["font"]
                        font_size = span["size"]
                        # Redact the original text
                        page.add_redact_annot(inst, fill=(1, 1, 1))
                        page.apply_redactions()
                        # Insert the replacement text with the same font and size
                        try:
                            if font_name in custom_fonts:
                                page.insert_text(inst[:2], replacement, fontfile=custom_fonts[font_name], fontsize=font_size, color=(0, 0, 0))
                            else:
                                page.insert_text(inst[:2], replacement, fontname=font_name, fontsize=font_size, color=(0, 0, 0))
                        except Exception as e:
                            print(f"Error using font {font_name}: {e}")
                            # Use a default font if the original font is not available
                            page.insert_text(inst[:2], replacement, fontname="helv", fontsize=font_size, color=(0, 0, 0))
    
    # Save the modified PDF to the output path
    pdf_document.save(output_pdf_path)
    pdf_document.close()

def replace_keywords_from_directory(directory_path, temp_directory, keyword_to_replace, replacement_value):
    # Ensure the temp directory exists
    os.makedirs(temp_directory, exist_ok=True)

    # Loop through all files in the directory
    for filename in os.listdir(directory_path):
        if filename.lower().endswith('.pdf'):
            input_pdf_path = os.path.join(directory_path, filename)
            temp_pdf_path = os.path.join(temp_directory, filename)

            # Replace keywords in the PDF
            replace_text_in_pdf(input_pdf_path, temp_pdf_path, keyword_to_replace, replacement_value)

            # Open the input PDF file to copy metadata
            with open(input_pdf_path, 'rb') as input_pdf_file:
                reader = PyPDF2.PdfReader(input_pdf_file)
                writer = PyPDF2.PdfWriter()

                # Read the modified PDF
                with open(temp_pdf_path, 'rb') as temp_pdf_file:
                    modified_reader = PyPDF2.PdfReader(temp_pdf_file)
                    for page_num in range(len(modified_reader.pages)):
                        writer.add_page(modified_reader.pages[page_num])

                # Replace metadata keywords
                metadata = reader.metadata
                if metadata:
                    new_metadata = {key: value.replace(keyword_to_replace, replacement_value) if isinstance(value, str) else value for key, value in metadata.items()}
                    writer.add_metadata(new_metadata)

                # Write the output PDF file with updated metadata
                with open(temp_pdf_path, 'wb') as temp_pdf_file:
                    writer.write(temp_pdf_file)

def display_metadata(reader):
    """Display metadata of the PDF file."""
    metadata = reader.metadata
    print("Metadata:")
    for key, value in metadata.items():
        print(f"{key}: {value}")

# Identify whether the directory_path exists
if not os.path.exists(directory_path):
    print(f"Directory {directory_path} does not exist. Creating it now.")
    # create the directory_path
    os.makedirs(directory_path, exist_ok=True)

# Identify whether the output_directory exists
if not os.path.exists(output_directory):
    print(f"Directory {output_directory} does not exist. Creating it now.")
    # create the output_directory
    os.makedirs(output_directory, exist_ok=True)

# Identify whether there are any PDF files in the directory_path
if not os.listdir(directory_path):
    print(f"Directory {directory_path} does not contain any PDF files. Please put some PDF files in this directory and try again.")
else:
    # Launch the replace_keywords_from_directory function
    replace_keywords_from_directory(directory_path, temp_directory, keyword_to_replace, replacement_value)
    print(f"Keyword {keyword_to_replace} in PDF content and metadata replaced with {replacement_value} for all files in {directory_path}")
    print(f"Output files saved temporarily to {temp_directory}")

    # Prompt for subsequent iterations
    continue_iterating = input("Do you want to replace other keywords (y/n): ")
    if continue_iterating.lower() == 'y':
        while continue_iterating.lower() == 'y':
            keyword_to_replace = input("Enter the keyword to replace: ")
            replacement_value = input("Enter the replacement value: ")
            replace_keywords_from_directory(temp_directory, temp_directory, keyword_to_replace, replacement_value)
            print(f"Keyword {keyword_to_replace} in PDF content and metadata replaced with {replacement_value} for all files in {directory_path}")
            print(f"Output files saved temporarily to {temp_directory}")
            continue_iterating = input("Do you want to replace other keywords (y/n): ")

    # Move the files from temp_directory to output_directory, overwriting if necessary
    for filename in os.listdir(temp_directory):
        src_path = os.path.join(temp_directory, filename)
        dst_path = os.path.join(output_directory, filename)
        if os.path.exists(dst_path):
            os.remove(dst_path)
        shutil.move(src_path, dst_path)
    print(f"Files moved from {temp_directory} to {output_directory}")