import os

# Set the folder path where your HTML, CSS, and JS files are stored
folder_path = 'C:/Users/tanis/OneDrive/Desktop/elegancfurniture.com'  # <-- replace this with your actual folder path

# Text to replace
old_text = "Premium Executive"
new_text = "Utopian Series"

# File extensions to consider
file_extensions = ('.html', '.css', '.js')

# Traverse all files in the directory
for root, _, files in os.walk(folder_path):
    for file_name in files:
        if file_name.endswith(file_extensions):
            file_path = os.path.join(root, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # Replace text if old_text is found
            if old_text in content:
                updated_content = content.replace(old_text, new_text)
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(updated_content)
                print(f"Updated: {file_path}")
