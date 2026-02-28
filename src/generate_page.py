import os
from markdown_to_html import markdown_to_html_node

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")

    with open(from_path, "r") as md_file:
        md_content = md_file.read()
    
    with open(template_path, "r") as tp_file:
        tp_content = tp_file.read()

    html_node = markdown_to_html_node(md_content)
    html_string = html_node.to_html()

    title = extract_title(md_content)

    content = tp_content.replace("{{ Title }}", title)
    html_content = content.replace("{{ Content }}", html_string)

    create_dest_folder_path(dest_path)

    with open(dest_path, "w") as html_file:
        html_file.write(html_content)

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.strip("#").strip()
    raise Exception("no title (h1 header) found")

def create_dest_folder_path(dest_path):
    dir_path = os.path.dirname(dest_path)
    os.makedirs(dir_path, exist_ok=True)