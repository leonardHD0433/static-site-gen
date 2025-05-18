import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_simple_title(self):
        markdown = "# Hello World"
        self.assertEqual(extract_title(markdown), "Hello World")
    
    def test_title_with_whitespace(self):
        markdown = "#    Spaced Title    "
        self.assertEqual(extract_title(markdown), "Spaced Title")
    
    def test_title_with_multiple_lines(self):
        markdown = "# Title Line\nThis is content\n## Subheading"
        self.assertEqual(extract_title(markdown), "Title Line")
    
    def test_no_title(self):
        markdown = "This is just content\n## Subheading"
        with self.assertRaises(Exception):
            extract_title(markdown)