from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError("Tag is required for parent nodes")
        if children is None:
            raise ValueError("Children is required for parent nodes")
        if not isinstance(children, list):
            raise ValueError("Children must be a list")
        if props is None:
            props = {}
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Tag is required for parent nodes")
        if self.children is None:
            raise ValueError("Children is required for parent nodes")
        
        children_html = "".join(child.to_html() for child in self.children)
        props_str = self.props_to_html()
        
        if props_str:
            return f"<{self.tag}{props_str}>{children_html}</{self.tag}>"
        return f"<{self.tag}>{children_html}</{self.tag}>" 