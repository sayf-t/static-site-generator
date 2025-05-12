import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_div(self):
        node = LeafNode("div", "Hello, world!")
        self.assertEqual(node.to_html(), "<div>Hello, world!</div>")

    def test_leaf_to_html_div_with_props(self):
        node = LeafNode("div", "Hello, world!", props={"class": "test"})
        self.assertEqual(node.to_html(), '<div class="test">Hello, world!</div>')

    def test_leaf_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode("div", None).to_html()

    def test_leaf_no_tag(self):
        node = LeafNode(None, "Just some text")
        self.assertEqual(node.to_html(), "Just some text")
             
if __name__ == "__main__":
    unittest.main()
        
        
        
        
        
        