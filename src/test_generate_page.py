import unittest
from generate_page import extract_title, generate_page

class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        md = """
# Hello! 
"""
        self.assertEqual(extract_title(md),
            "Hello!"                 
        )

    def test_extract_title_no_h1(self):
        md = """
## There is no h1 here.
Only a h2.
"""
        with self.assertRaises(Exception):
            title = extract_title(md)

    def test_double_title(self):
        md = """
# This is a title

# This is a second title that should be ignored
"""

        self.assertEqual(extract_title(md), 
            "This is a title"
        )