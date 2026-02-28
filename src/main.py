import os
from copy_static import copy_files
from generate_page import generate_page

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    
    copy_files(dir_path_static, dir_path_public)
    print("Copied static files to public directory.")

    generate_page(
        os.path.join(dir_path_content, "index.md"),
        template_path,
        os.path.join(dir_path_public, "index.html")
    )
    print("Page generated successfully.")

if __name__ == "__main__":
    main()
