import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        child1 = LeafNode("p", "First")
        child2 = LeafNode("p", "Second")
        parent_node = ParentNode("div", [child1, child2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><p>First</p><p>Second</p></div>",
        )

    def test_to_html_with_no_children(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")

    def test_to_html_with_props(self):
        child_node = LeafNode("p", "content")
        parent_node = ParentNode("div", [child_node], {"class": "container"})
        self.assertEqual(
            parent_node.to_html(),
            '<div class="container"><p>content</p></div>',
        )

    def test_to_html_with_none_children(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None)

    def test_to_html_with_invalid_children_type(self):
        with self.assertRaises(ValueError):
            ParentNode("div", "not a list")

    # New edge cases and complex scenarios
    def test_deeply_nested_structure(self):
        leaf1 = LeafNode("span", "text1")
        leaf2 = LeafNode("em", "text2")
        leaf3 = LeafNode("strong", "text3")
        
        inner_parent = ParentNode("p", [leaf1, leaf2])
        middle_parent = ParentNode("div", [inner_parent, leaf3])
        outer_parent = ParentNode("section", [middle_parent])
        
        self.assertEqual(
            outer_parent.to_html(),
            "<section><div><p><span>text1</span><em>text2</em></p><strong>text3</strong></div></section>"
        )

    def test_mixed_leaf_and_parent_children(self):
        text_node = LeafNode(None, "plain text")
        parent_with_child = ParentNode("span", [LeafNode("em", "emphasized")])
        leaf_node = LeafNode("b", "bold")
        
        parent = ParentNode("div", [text_node, parent_with_child, leaf_node])
        self.assertEqual(
            parent.to_html(),
            "<div>plain text<span><em>emphasized</em></span><b>bold</b></div>"
        )

    def test_multiple_nested_props(self):
        inner = ParentNode("p", [LeafNode("span", "text")], {"class": "inner", "id": "p1"})
        outer = ParentNode("div", [inner], {"class": "outer", "data-test": "true"})
        self.assertEqual(
            outer.to_html(),
            '<div class="outer" data-test="true"><p class="inner" id="p1"><span>text</span></p></div>'
        )

    def test_empty_nested_parents(self):
        inner = ParentNode("div", [])
        middle = ParentNode("span", [inner])
        outer = ParentNode("section", [middle])
        self.assertEqual(
            outer.to_html(),
            "<section><span><div></div></span></section>"
        )

    def test_many_siblings(self):
        children = [LeafNode("span", str(i)) for i in range(10)]
        parent = ParentNode("div", children)
        expected = "<div>" + "".join(f"<span>{i}</span>" for i in range(10)) + "</div>"
        self.assertEqual(parent.to_html(), expected)

    def test_parent_with_text_only_children(self):
        children = [LeafNode(None, "text1"), LeafNode(None, "text2"), LeafNode(None, "text3")]
        parent = ParentNode("p", children)
        self.assertEqual(parent.to_html(), "<p>text1text2text3</p>")

if __name__ == "__main__":
    unittest.main() 