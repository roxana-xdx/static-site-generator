import unittest
from htmlnode import HTMLNode

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

if __name__ == "__main__":
    unitttest.main()