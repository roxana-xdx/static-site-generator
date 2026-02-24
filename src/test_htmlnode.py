import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_no_children(self):
        node = ParentNode("span", [])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_with_multiple_children(self):
        child_node1 = LeafNode("span", "child 1")
        child_node2 = LeafNode("b", "child 2")
        child_node3 = LeafNode(None, "child 3")
        parent_node = ParentNode("div", [child_node1, child_node2, child_node3])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child 1</span><b>child 2</b>child 3</div>",
        )

if __name__ == "__main__":
    unitttest.main()
