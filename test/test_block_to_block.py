import unittest
from block_type import BlockType
from block_to_block import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    
    def test_paragraph(self):
        # Test regular paragraph
        markdown = "This is a regular paragraph."
        self.assertEqual(block_to_block_type(markdown), BlockType.PARAGRAPH)
        
        # Test multi-line paragraph
        markdown = "This is a paragraph\nwith multiple lines."
        self.assertEqual(block_to_block_type(markdown), BlockType.PARAGRAPH)
    
    def test_heading(self):
        # Test h1 heading
        markdown = "# This is a heading"
        self.assertEqual(block_to_block_type(markdown), BlockType.HEADING)
        
        # Test h6 heading
        markdown = "###### This is another heading"
        self.assertEqual(block_to_block_type(markdown), BlockType.HEADING)
        
        # Test invalid heading (no space after #)
        markdown = "#This is not a valid heading"
        self.assertEqual(block_to_block_type(markdown), BlockType.PARAGRAPH)
        
        # Test invalid heading (more than 6 #)
        markdown = "####### Too many hashtags"
        self.assertEqual(block_to_block_type(markdown), BlockType.PARAGRAPH)
    
    def test_code(self):
        # Test code block
        markdown = "```\nprint('Hello World!')\n```"
        self.assertEqual(block_to_block_type(markdown), BlockType.CODE)
        
        # Test code block with language specified
        markdown = "```python\nprint('Hello World!')\n```"
        self.assertEqual(block_to_block_type(markdown), BlockType.CODE)

    def test_quote(self):
        # Test single line quote
        markdown = ">This is a quote"
        self.assertEqual(block_to_block_type(markdown), BlockType.QUOTE)
        
        # Test multi-line quote
        markdown = ">First line\n>Second line\n>Third line"
        self.assertEqual(block_to_block_type(markdown), BlockType.QUOTE)
        
        # Test invalid quote (missing > on second line)
        markdown = ">First line\nSecond line"
        self.assertEqual(block_to_block_type(markdown), BlockType.PARAGRAPH)
    
    def test_unordered_list(self):
        # Test single item list
        markdown = "- Item one"
        self.assertEqual(block_to_block_type(markdown), BlockType.UNORDERED_LIST)
        
        # Test multi-item list
        markdown = "- Item one\n- Item two\n- Item three"
        self.assertEqual(block_to_block_type(markdown), BlockType.UNORDERED_LIST)
        
        # Test invalid list (missing space after -)
        markdown = "-Item one"
        self.assertEqual(block_to_block_type(markdown), BlockType.PARAGRAPH)
        
        # Test invalid list (missing - on second line)
        markdown = "- Item one\nItem two"
        self.assertEqual(block_to_block_type(markdown), BlockType.PARAGRAPH)

    def test_ordered_list(self):
        # Test single item list
        markdown = "1. Item one"
        self.assertEqual(block_to_block_type(markdown), BlockType.ORDERED_LIST)
        
        # Test multi-item list
        markdown = "1. Item one\n2. Item two\n3. Item three"
        self.assertEqual(block_to_block_type(markdown), BlockType.ORDERED_LIST)
        
        # Test invalid list (wrong order)
        markdown = "1. Item one\n3. Item two"
        self.assertEqual(block_to_block_type(markdown), BlockType.PARAGRAPH)
        
        # Test invalid list (not starting with 1)
        markdown = "2. Item one\n3. Item two"
        self.assertEqual(block_to_block_type(markdown), BlockType.PARAGRAPH)
        
        # Test invalid list (missing space after number)
        markdown = "1.Item one"
        self.assertEqual(block_to_block_type(markdown), BlockType.PARAGRAPH)