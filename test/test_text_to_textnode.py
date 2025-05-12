import unittest
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes

class TestTextToTextNode(unittest.TestCase):
    def test_text(self):
        node = text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            node,
        )

    def test_bold_only(self):
        nodes = text_to_textnodes("This has **bold** text only")
        self.assertListEqual(
            [
                TextNode("This has ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text only", TextType.TEXT),
            ],
            nodes
        )

    def test_italic_only(self):
        nodes = text_to_textnodes("This has _italic_ text only")
        self.assertListEqual(
            [
                TextNode("This has ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text only", TextType.TEXT),
            ],
            nodes
        )

    def test_code_only(self):
        nodes = text_to_textnodes("This has `code` text only")
        self.assertListEqual(
            [
                TextNode("This has ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" text only", TextType.TEXT),
            ],
            nodes
        )

    def test_image_only(self):
        nodes = text_to_textnodes("This has ![an image](https://example.com/img.jpg) only")
        self.assertListEqual(
            [
                TextNode("This has ", TextType.TEXT),
                TextNode("an image", TextType.IMAGE, "https://example.com/img.jpg"),
                TextNode(" only", TextType.TEXT),
            ],
            nodes
        )

    def test_link_only(self):
        nodes = text_to_textnodes("This has [a link](https://example.com) only")
        self.assertListEqual(
            [
                TextNode("This has ", TextType.TEXT),
                TextNode("a link", TextType.LINK, "https://example.com"),
                TextNode(" only", TextType.TEXT),
            ],
            nodes
        )

    def test_empty_string(self):
        nodes = text_to_textnodes("")
        self.assertListEqual(
            [],
            nodes
        )

    def test_multiple_same_formatting(self):
        # Test multiple bold sections
        nodes = text_to_textnodes("This has **multiple** bold **sections**")
        self.assertListEqual(
            [
                TextNode("This has ", TextType.TEXT),
                TextNode("multiple", TextType.BOLD),
                TextNode(" bold ", TextType.TEXT),
                TextNode("sections", TextType.BOLD),
            ],
            nodes
        )
        
        # Test multiple italic sections
        nodes = text_to_textnodes("This has _multiple_ italic _sections_")
        self.assertListEqual(
            [
                TextNode("This has ", TextType.TEXT),
                TextNode("multiple", TextType.ITALIC),
                TextNode(" italic ", TextType.TEXT),
                TextNode("sections", TextType.ITALIC),
            ],
            nodes
        )
        # Test multiple code sections
        nodes = text_to_textnodes("This has `multiple` code `sections`")
        self.assertListEqual(
            [
                TextNode("This has ", TextType.TEXT),
                TextNode("multiple", TextType.CODE),
                TextNode(" code ", TextType.TEXT),
                TextNode("sections", TextType.CODE),
            ],
            nodes
        )
        # Test multiple image sections
        nodes = text_to_textnodes("This has ![alt text 1](url1) and ![alt text 2](url2)")
        self.assertListEqual(
            [
                TextNode("This has ", TextType.TEXT),
                TextNode("alt text 1", TextType.IMAGE, "url1"),
                TextNode(" and ", TextType.TEXT),
                TextNode("alt text 2", TextType.IMAGE, "url2"),
            ],
            nodes
        )
        # Test multiple link sections
        nodes = text_to_textnodes("This has [link 1](url1) and [link 2](url2)")
        self.assertListEqual(
            [
                TextNode("This has ", TextType.TEXT),
                TextNode("link 1", TextType.LINK, "url1"),
                TextNode(" and ", TextType.TEXT),
                TextNode("link 2", TextType.LINK, "url2"),
            ],
            nodes
        )