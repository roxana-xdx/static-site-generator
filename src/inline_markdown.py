import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise Exception("matching delimiter not found")
        
        for i in range(len(parts)):
            if parts[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(parts[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(parts[i], text_type))
            
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            new_nodes.append(node)
            continue

        remaining_text = node.text
        for image in images:
            parts = remaining_text.split(f"![{image[0]}]({image[1]})", 1)

            if len(parts) != 2:
                raise ValueError("invalid markdown, image section not closed")
        
            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))

            remaining_text = parts[1]

        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
            
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            new_nodes.append(node)
            continue

        remaining_text = node.text
        for link in links:
            parts = remaining_text.split(f"[{link[0]}]({link[1]})", 1)

            if len(parts) != 2:
                raise ValueError("invalid markdown, link section not closed")
        
            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            
            remaining_text = parts[1]

        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
            
    return new_nodes