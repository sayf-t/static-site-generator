import unittest

from textnode import TextNode, TextType, text_node_to_html_node

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

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

    def test_italic(self):
        node = TextNode("This is italic", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is italic")
        
if __name__ == "__main__":
    unittest.main()