from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    block_strings = markdown.split("\n\n")
    new_blocks = []
    for string in block_strings:
        new_string = string.strip()
        if new_string != "":
            new_blocks.append(new_string)
    return new_blocks

def block_to_block_type(markdown):
    lines = re.findall(r"^#{1,6} .+", markdown)
    if len(lines) != 0:
        return BlockType.HEADING
    
    lines = re.findall(r"^```\n(.|\n)+\n```", markdown)
    if len(lines) != 0:
        return BlockType.CODE
    
    lines = re.findall(r"(^> ?.+\n)+", markdown)
    if len(lines) != 0:
        return BlockType.QUOTE
    
    lines = re.findall(r"(^- .+)+", markdown)
    if len(lines) != 0:
        return BlockType.UNORDERED_LIST
    
    lines = re.findall(r"(^\d+\. .+)+", markdown)
    if len(lines) != 0:
        ordered = True
        for i in range(len(lines)):
            if not lines[i].startswith(f"{i+1}. "):
                ordered = False
        if ordered:
            return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
    