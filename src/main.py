from copy_static import copy_files

dir_path_static = "./static"
dir_path_public = "./public"

def main():
    
    copy_files(dir_path_static, dir_path_public)
    print("Successfully copied static files to public directory.")

if __name__ == "__main__":
    main()
