import unittest
from parentnode import ParentNode
from leafnode import LeafNode

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

    def test_to_html_missing_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, []).to_html()

    def test_to_html_missing_children(self):
        with self.assertRaises(ValueError) as context:
            ParentNode("div", None).to_html()
        self.assertEqual(str(context.exception), "Y no children?")

    def test_to_html_empty_children(self):
        node = ParentNode("div", [])
        self.assertEqual(node.to_html(), "<div></div>")

    def test_to_html_with_single_prop(self):
        node = ParentNode("div", [], props={"class": "single-class"})
        self.assertEqual(node.to_html(), '<div class="single-class"></div>')

    def test_to_html_with_multiple_props(self):
        node = ParentNode("div", [], props={"class": "container", "id": "main"})
        self.assertEqual(
            node.to_html(),
            '<div class="container" id="main"></div>'
        )

    def test_to_html_with_props_and_children(self):
        child = LeafNode("span", "child text")
        node = ParentNode("div", [child], props={"class": "container"})
        self.assertEqual(
            node.to_html(),
            '<div class="container"><span>child text</span></div>'
        )

    def test_to_html_with_deeply_nested_nodes(self):
        # Create a deeply nested HTML structure
        deepest_node = LeafNode("i", "deep")  # Innermost node
        inner_node = ParentNode("span", [deepest_node])  # Nested inside <span>
        middle_node = ParentNode("div", [inner_node])  # Nested inside <div>
        outer_node = ParentNode("section", [middle_node])  # Nested inside <section>
        
        # Expected HTML output
        expected_html = "<section><div><span><i>deep</i></span></div></section>"
        
        # Assert the output is correct
        self.assertEqual(outer_node.to_html(), expected_html)