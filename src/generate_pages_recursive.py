import os
from generate_page import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    entries= os.listdir(dir_path_content)

    # Ensure destination directory exists
    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path)

    for entry in entries:
        entry_path = os.path.join(dir_path_content, entry)

        if os.path.isfile(entry_path): # if it is file
            if entry.endswith(".md"):
                base_name = os.path.splitext(entry)[0]
                output_path = os.path.join(dest_dir_path, base_name + ".html")
                generate_page(entry_path, template_path, output_path)

        else: # if it is directory
            new_dest_dir_path = os.path.join(dest_dir_path, entry)
            
            # Ensure the new directory exists
            if not os.path.exists(new_dest_dir_path):
                os.makedirs(new_dest_dir_path)

            generate_pages_recursive(entry_path, template_path, new_dest_dir_path )

generate_pages_recursive("content", "template.html", "public")