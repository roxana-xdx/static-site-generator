import os, sys
from copy_static import copy_files
from generate_page import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    copy_files(dir_path_static, dir_path_public)
    print("Copied static files to public directory.")

    generate_pages_recursive(
        dir_path_content,
        template_path,
        dir_path_public,
        basepath,
    )
    print("Pages generated successfully.")

if __name__ == "__main__":
    main()
