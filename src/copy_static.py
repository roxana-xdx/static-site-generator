import os
import shutil

def copy_files(source_dir, dest_dir):
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    os.mkdir(dest_dir)

    items = os.listdir(source_dir)
    for item in items:
        file_path = os.path.join(source_dir, item)
        
        if os.path.isfile(file_path):
            shutil.copy(file_path, dest_dir)

        elif os.path.isdir(file_path):
            new_dir = os.path.join(dest_dir, item)
            copy_files(file_path, new_dir)