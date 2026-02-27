import unittest
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes
)
from textnode import TextNode, TextType

class TestInlineMarkdown(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(new_nodes,
            [TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
            ]             
        )

    def test_split_bold_twice(self):
        node = TextNode("This is text with **even two** bolded **words**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(new_nodes,
            [TextNode("This is text with ", TextType.TEXT),
            TextNode("even two", TextType.BOLD),
            TextNode(" bolded ", TextType.TEXT),
            TextNode("words", TextType.BOLD),
            ]             
        )

    def test_split_bold_and_italic(self):
        node = TextNode("This text has **bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertEqual(
            [
                TextNode("This text has ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_extract_images(self):
        text = "This is a text with an ![image example](https://imagelink.com/path-123ABC.gif) and ![another image](https://sub.domain.com/folder1.jpg) and a [link](https://link.com/link123)"
        matches = extract_markdown_images(text)
        self.assertListEqual(
            matches, [("image example", "https://imagelink.com/path-123ABC.gif"), ("another image", "https://sub.domain.com/folder1.jpg")]
            )
    
    def test_extract_links(self):
        text = "This is a text with a [link example](https://link.com/path-123ABC.link) and [another link](https://sub.domain.com/folder1/path.ABC@d-E_f#g) and an ![image](https://image.com/img.jpg)"

        matches = extract_markdown_links(text)
        self.assertListEqual(
            matches, [("link example", "https://link.com/path-123ABC.link"), ("another link", "https://sub.domain.com/folder1/path.ABC@d-E_f#g")]
            )

    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.image.com/abc123.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.image.com/abc123.png"),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode("This is text with an ![image](https://i.image.com/xYz123.png) and another ![second image](https://example.com/Test.jpg)",
        TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.image.com/xYz123.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://example.com/Test.jpg"
            ),
            ]
        )

    def test_split_links(self):
        node = TextNode("This is text with a [link](https://link.com/xYz123.png) and [another link](https://example.com/Test#link) example",
        TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://link.com/xYz123.png"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "another link", TextType.LINK, "https://example.com/Test#link"
            ),
            TextNode(" example", TextType.TEXT),
            ]
        )

    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![example image](https://i.image.com/eX4MpL3.png) and a [link](https://boot.dev)"

        self.assertListEqual(text_to_textnodes(text),
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("example image", TextType.IMAGE, "https://i.image.com/eX4MpL3.png"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ]    
        )