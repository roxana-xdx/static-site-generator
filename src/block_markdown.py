def markdown_to_blocks(markdown):
    block_strings = markdown.split("\n\n")
    new_blocks = []
    for string in block_strings:
        new_string = string.strip()
        if new_string != "":
            new_blocks.append(new_string)
    return new_blocks