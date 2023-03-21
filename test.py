import os
import re

# define the folder path
folder_path = "./_posts/"

# loop through all files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith(".md"):
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, "r", encoding="utf-8") as f:
            file_contents = f.read()

        # find the categories field in the file contents
        categories_match = re.search(r"categories:\s*\[(.*?)\]", file_contents)
        if categories_match:
            categories = categories_match.group(1).split(",")
            categories = [c.strip() for c in categories]

            # remove the ACGN category if it exists
            if "ACGN" in categories:
                categories.remove("ACGN")

            # write the updated categories field to the file
            updated_categories = "[{}]".format(",".join(categories))
            updated_contents = re.sub(r"categories:\s*\[(.*?)\]", "categories: {}".format(updated_categories), file_contents)

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(updated_contents)