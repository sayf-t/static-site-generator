from textnode import TextNode, TextType
from leafnode import LeafNode

def text_node_to_html_node(text_node):
    if text_node.type == TextType.NORMAL_TEXT:
        return LeafNode(tag=None, value=text_node.text)
    elif text_node.type == TextType.BOLD:
        return LeafNode(tag="b", value=text_node.text)
    elif text_node.type == TextType.ITALIC:
        return LeafNode(tag="i", value=text_node.text)
    elif text_node.type == TextType.CODE:
        return LeafNode(tag="code", value=text_node.text)
    elif text_node.type == TextType.LINK:
        return LeafNode(tag="a", value=text_node.text, url=text_node.url)
    elif text_node.type == TextType.IMAGE:
        return LeafNode(tag="img", value=text_node.text, url=text_node.url)
    else:
        raise ValueError(f"Unknown text node type: {text_node.type}")
