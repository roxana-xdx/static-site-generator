import unittest
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_several_newlines(self):
        md = """
This is **bolded** paragraph


This is another paragraph with _italic_ text and `code` here



This is another paragraph
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here",
                "This is another paragraph",
            ],
        )

    def test_block_to_block_type_heading(self):
        md = "# Heading 1"
        self.assertEqual(block_to_block_type(md), BlockType.HEADING)

        md = "###### Heading 6 example"
        self.assertEqual(block_to_block_type(md), BlockType.HEADING)

        md = "#This is not a Heading"
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

    def test_block_to_block_type_multiline_code(self):
        md = """```
Multiline code example
```"""
        self.assertEqual(block_to_block_type(md), BlockType.CODE)

        md = """```
```"""
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

        md = """```
This isn't a proper code block
``"""
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

    def test_block_to_block_type_quote(self):
        md = """> This is a quote!
>This is the second part of the quote."""
        self.assertEqual(block_to_block_type(md), BlockType.QUOTE)

    def test_block_to_block_unordered_list(self):
        md = """- This is
- a valid
- unordered list."""
        self.assertEqual(block_to_block_type(md), BlockType.UNORDERED_LIST)

        md = """-This is NOT
-a valid list."""
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

    def test_block_to_block_ordered_list(self):
        md = "1. This is an ordered list."
        self.assertEqual(block_to_block_type(md), BlockType.ORDERED_LIST)

        md = """1. This is another ordered list
2. With 2 items!"""
        self.assertEqual(block_to_block_type(md), BlockType.ORDERED_LIST)

        md = """1.This is not a valid ordered list
2. Spaces are (sometimes) important in markdown"""
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

        md = """2. This is not a valid ordered list
1. Order matters!"""
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)
