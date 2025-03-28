import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_none(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)


    def test_props_to_html(self):
        test_props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }

        test_string = " href=\"https://www.google.com\" target=\"_blank\""
        node = HTMLNode(props=test_props)
        self.assertEqual(node.props_to_html(), test_string)

    def test_repr(self):
        node = HTMLNode("F","U","C", {"K": "this is a swear word"})
        test_string = "\nTag: F\nValue: U\nChildren: C\nProps: {'K': 'this is a swear word'}"
        self.assertEqual(node.__repr__(), test_string)


if __name__ == "__main__":
    unittest.main()