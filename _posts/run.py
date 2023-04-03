import os

# set the path to the directory containing the .md files
path = './'

# loop through each file in the directory
for filename in os.listdir(path):
    if filename.endswith('.md'):
        # open the file with the correct encoding
        with open(os.path.join(path, filename), 'r', encoding='utf-8') as file:
            content = file.readlines()

        # add the permalink to the YAML front matter
        permalink = 'permalink: /posts/{}/\n'.format(filename[:-3])
        content.insert(4, permalink)

        # write the updated content back to the file with the correct encoding
        with open(os.path.join(path, filename), 'w', encoding='utf-8') as file:
            file.writelines(content)