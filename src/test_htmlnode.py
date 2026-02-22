import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_values(self):
        node = HTMLNode("div", "Text",)
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Text")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_props_to_html(self):
        node = HTMLNode("div", "Hello, world!", None, {"class": "greeting"},)
        self.assertEqual(node.props_to_html(), " class=\"greeting\"")

    def test_repr(self):
        node = HTMLNode("p", "Text", None, {"class": "example"})
        self.assertEqual(
             repr(node),
            "HTMLNode(p, Text, None, {'class': 'example'})"
        )

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click here.",
                        {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            "<a href=\"https://www.google.com\">Click here.</a>"
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_repr(self):
        node = LeafNode("p", "Text", {"class": "example"})
        self.assertEqual(
            repr(node),
            "LeafNode(p, Text, {'class': 'example'})"
        )

if __name__ == "__main__":
    unitttest.main()