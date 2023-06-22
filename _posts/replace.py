import os

def replace_categories_with_tags(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        if line.strip().startswith('categories: ['):
            modified_lines.append(line.replace('categories:', 'tags:'))
        else:
            modified_lines.append(line)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(modified_lines)

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):  # Update the file extension as needed
                file_path = os.path.join(root, file)
                replace_categories_with_tags(file_path)
                print(f"Modified: {file_path}")

# Main entry point
if __name__ == '__main__':
    directory = './'  # Update the directory path as needed
    process_directory(directory)
