import unittest
from markdown_to_htmlnode import markdown_to_html_node

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = "This is just a normal paragraph."
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is just a normal paragraph.</p></div>"
        )

        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

        md = """
```
print('Hello, world!')
print('Blank line above')
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>print('Hello, world!')\nprint('Blank line above')\n</code></pre></div>",
        )

    def test_heading(self):
        md = "# My Heading"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>My Heading</h1></div>"
        )

        md = "## My Heading"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h2>My Heading</h2></div>"
        )

        md = "#### My Heading"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h4>My Heading</h4></div>"
        )

        md = "###### My Heading"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h6>My Heading</h6></div>"
        )

        md = "#My Heading"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>#My Heading</p></div>"
        )

        md = "####### My Heading"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>####### My Heading</p></div>"
        )

    def test_quote_block(self):
        md = "> This is a quote"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote</blockquote></div>"
        )
    
        md = """
> This is a multi-line
> quote with **bold** and _italic_ text
> and some `code` too
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a multi-line quote with <b>bold</b> and <i>italic</i> text and some <code>code</code> too</blockquote></div>"
        )
    
        md = """
> Nested quotes are interesting
>
> They can contain multiple paragraphs
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>Nested quotes are interesting\n\nThey can contain multiple paragraphs</blockquote></div>"
        )

    def test_ordered_list_block(self):
        md = "1. First Item"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html, 
            "<div><ol><li>First Item</li></ol></div>"
        )

        md = "1. First Item\n2. Second Item"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html, 
            "<div><ol><li>First Item</li><li>Second Item</li></ol></div>"
        )

        md = """
1. This item has **bold** text
2. This item has _italic_ text
3. This one has `code` as well
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html, 
            "<div><ol><li>This item has <b>bold</b> text</li><li>This item has <i>italic</i> text</li><li>This one has <code>code</code> as well</li></ol></div>"
        )

    def test_unordered_list_block(self):
        md = "- Item one"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html, 
            "<div><ul><li>Item one</li></ul></div>"
        )

        md = "- Item one\n- Item two\n- Item three"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html, 
            "<div><ul><li>Item one</li><li>Item two</li><li>Item three</li></ul></div>"
        )

        
