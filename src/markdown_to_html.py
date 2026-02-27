from htmlnode import ParentNode, LeafNode
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType

def markdown_to_html_node(markdown):
    """
    converts a markdown document into a parent HTMLNode, which contains child HTMLNode objects representing the nested elements
    """

    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            inline_html = text_to_children(block.replace("\n", " "))
            node = ParentNode("p", inline_html)

        elif block_type == BlockType.HEADING:
            heading_level = 0
            i = 0
            while block[i] == "#":
                heading_level += 1
                i += 1
            inline_html = text_to_children(block[heading_level+1:])
            node = ParentNode(f"h{heading_level}", inline_html)

        elif block_type == BlockType.CODE:
            text = block[4:-3]
            text_node = TextNode(text, TextType.CODE)
            code_node = text_node_to_html_node(text_node)
            node = ParentNode("pre", [code_node])

        elif block_type == BlockType.QUOTE:
            lines = block.split("\n")
            new_lines = []
            for line in lines:
                new_lines.append(line[1:].strip())
            block = " ".join(new_lines)

            inline_html = text_to_children(block)
            node = ParentNode("blockquote", inline_html)

        elif block_type == BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            list_items = []
            for line in lines:
                list_item = line[1:].strip()
                inline_html = text_to_children(list_item)
                list_items.append(ParentNode("li", inline_html))
            node = ParentNode("ul", list_items)

        elif block_type == BlockType.ORDERED_LIST:
            lines = block.split("\n")
            list_items = []
            for line in lines:
                i = 0
                while line[i] != ".":
                    i += 1
                list_item = line[i+1:].strip()
                inline_html = text_to_children(list_item)
                list_items.append(ParentNode("li", inline_html))
            node = ParentNode("ol", list_items)

        children.append(node)
        
    return ParentNode("div", children)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        children.append(html_node)
    return children