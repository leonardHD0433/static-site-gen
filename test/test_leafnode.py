import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_prop(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        node2 = LeafNode("button", "Click me!", {"class": "btn-primary", "id": "submit-btn"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")
        self.assertEqual(node2.to_html(), '<button class="btn-primary" id="submit-btn">Click me!</button>')

    def test_to_html_missing_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None).to_html()

    def test_to_html_missing_tag(self):
        node = LeafNode(None, "Raw text here")
        self.assertEqual(node.to_html(), "Raw text here")

    def test_with_empty_attributes(self):
        node = LeafNode("span", "Text only", {})
        self.assertEqual(node.to_html(), "<span>Text only</span>")
    