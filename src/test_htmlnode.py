import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_htmlnode_repr(self):
        html_node = HTMLNode("div", "Hello, world!")
        self.assertEqual(str(html_node), "HTMLNode(tag=div, value=Hello, world!, children=None, props=None)")

    def test_htmlnode_to_html(self):
        # html_node = HTMLNode("div", "Hello, world!")
        # self.assertEqual(html_node.to_html(), "<div>Hello, world!</div>")
        pass

    def test_htmlnode_props_to_html(self):
        html_node = HTMLNode("div", "Hello, world!", props={"class": "test"})
        self.assertEqual(html_node.props_to_html(), ' class="test"')

if __name__ == "__main__":
    unittest.main()