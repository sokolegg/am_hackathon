import os
import re
from bs4 import BeautifulSoup

def clean_html(html_content):
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Remove all script and style elements
    for element in soup(['script', 'style', 'footer', 'header', 'nav', 'aside']):
        element.decompose()

    # Get the HTML content without script/style tags but still with other tags
    html_without_scripts = str(soup)

    # Use a regular expression to replace all HTML tags with a \n instead of h1, h2, h3, p, etc.
    # replace h1 with \n\n\n
    clean_text = re.sub(r'<h1[^>]*>', '\n\n\n', html_without_scripts)
    # replace h2 with \n\n
    clean_text = re.sub(r'<h2[^>]*>', '\n\n', clean_text)
    # replace h3 with \n
    clean_text = re.sub(r'<h3[^>]*>', '\n', clean_text)

    clean_text = re.sub(r'<[^>]+>', '\n', clean_text)

    # Replace multiple more than 2 space with \n
    # clean_text = re.sub(r'\s{2,}', '\n', clean_text)
    # replace   with space
    clean_text = clean_text.replace(u' ', u' ')


    # Strip leading and trailing spaces
    clean_text = clean_text.strip()

    return clean_text

def process_html_files_in_folder(folder_path):
    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".html") or filename.endswith(".htm"):
            file_path = os.path.join(folder_path, filename)

            # Read the HTML content from the file
            with open(file_path, 'r', encoding='utf-8') as file:
                html_content = file.read()

            # Clean the HTML content
            cleaned_text = clean_html(html_content)

            # Create a new filename by in folder nhs_pages_txt as txt file
            new_folder_path = folder_path.replace('nhs_pages', 'nhs_pages_txt')
            # create folder
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            new_filename = filename.replace(".html", ".txt")
            new_file_path = os.path.join(new_folder_path, new_filename)

            # Save the cleaned text to a new file
            with open(new_file_path, 'w', encoding='utf-8') as file:
                file.write(cleaned_text)

            print(f"Processed: {filename} -> {new_filename}")

# Example usage:
if __name__ == "__main__":
    folder_path = 'data/nhs_pages/'  # Replace with the path to your folder containing HTML files
    process_html_files_in_folder(folder_path)
