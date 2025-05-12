import unittest
from textnode import TextNode, TextType
from split_node import split_nodes_image, split_nodes_link

class TestSplitNodes(unittest.TestCase):
    def test_split_images_empty_text(self):
        node = TextNode("", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes)
    
    def test_split_images_no_image(self):
        node = TextNode(
            "This is text with no images in it.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [node],  # Should return the original node
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png), yay!",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(", yay!", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_images_multiple_nodes(self):
        node1 = TextNode("Text with ![img](url1)", TextType.TEXT)
        node2 = TextNode("Another text with ![img2](url2)", TextType.TEXT)
        new_nodes = split_nodes_image([node1, node2])
        self.assertListEqual(
            [
                TextNode("Text with ", TextType.TEXT),
                TextNode("img", TextType.IMAGE, "url1"),
                TextNode("Another text with ", TextType.TEXT),
                TextNode("img2", TextType.IMAGE, "url2"),
            ],
            new_nodes,
        )

    def test_split_images_consecutive(self):
        node = TextNode(
            "![img1](url1)![img2](url2)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("img1", TextType.IMAGE, "url1"),
                TextNode("img2", TextType.IMAGE, "url2"),
            ],
            new_nodes,
        )

    def test_split_links_no_link(self):
        node = TextNode(
            "This is text with no links in it.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [node],  # Should return the original node
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link to somewhere](https://example.com) and [another link](https://another-example.com) in it.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link to somewhere", TextType.LINK, "https://example.com"),
                TextNode(" and ", TextType.TEXT),
                TextNode("another link", TextType.LINK, "https://another-example.com"),
                TextNode(" in it.", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_links_empty_text(self):
        node = TextNode("", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)

    def test_split_links_multiple_nodes(self):
        node1 = TextNode("Text with [label1](url1)", TextType.TEXT)
        node2 = TextNode("Another text with [label2](url2)", TextType.TEXT)
        new_nodes = split_nodes_link([node1, node2])
        self.assertListEqual(
            [
                TextNode("Text with ", TextType.TEXT),
                TextNode("label1", TextType.LINK, "url1"),
                TextNode("Another text with ", TextType.TEXT),
                TextNode("label2", TextType.LINK, "url2"),
            ],
            new_nodes,
        )

    def test_split_links_consecutive(self):
        node = TextNode(
            "[label1](url1)[label2](url2)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("label1", TextType.LINK, "url1"),
                TextNode("label2", TextType.LINK, "url2"),
            ],
            new_nodes,
        )