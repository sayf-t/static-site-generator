import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_textnode_equality(self):
        text_node1 = TextNode("This is a text node", TextType.BOLD)
        text_node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(text_node1, text_node2)

    def test_textnode_inequality(self):
        text_node1 = TextNode("This is a text node", TextType.BOLD)
        text_node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(text_node1, text_node2)

    def test_textnode_inequality_different_type(self):
        text_node1 = TextNode("This is a text node", TextType.BOLD)
        text_node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(text_node1, text_node2)

    def test_textnode_with_url_equality(self):
        text_node1 = TextNode("Link text", TextType.LINK, "https://example.com")
        text_node2 = TextNode("Link text", TextType.LINK, "https://example.com")
        self.assertEqual(text_node1, text_node2)

    def test_textnode_with_different_urls(self):
        text_node1 = TextNode("Link text", TextType.LINK, "https://example.com")
        text_node2 = TextNode("Link text", TextType.LINK, "https://different.com")
        self.assertNotEqual(text_node1, text_node2)

    def test_textnode_none_url_equality(self):
        text_node1 = TextNode("Normal text", TextType.NORMAL_TEXT, None)
        text_node2 = TextNode("Normal text", TextType.NORMAL_TEXT, None)
        self.assertEqual(text_node1, text_node2)

    def test_textnode_none_vs_url(self):
        text_node1 = TextNode("Link text", TextType.LINK, None)
        text_node2 = TextNode("Link text", TextType.LINK, "https://example.com")
        self.assertNotEqual(text_node1, text_node2)

if __name__ == "__main__":
    unittest.main()