from textnode import TextType, TextNode

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("")
    
    def props_to_html(self):
        if not self.props:
            return ""
        
        props_str = ""
        for key, value in self.props.items():
            props_str += f' {key}="{value}"'
    
        return props_str
        
    def __repr__(self):
        return f"""
        tag = {self.tag}
        value = {self.value}
        children = {self.children}
        props = {self.props}"""
    
    def text_node_to_html_node(text_node):
        if text_node.text_type == TextType.TEXT:
            return LeafNode(None, text_node.text)
        elif text_node.text_type == TextType.BOLD:
            return LeafNode("b", text_node.text)
        elif text_node.text_type == TextType.ITALIC:
            return LeafNode("i", text_node.text)
        elif text_node.text_type == TextType.CODE:
            return LeafNode("code", text_node.text)
        elif text_node.text_type == TextType.LINK:
            props = {"href": text_node.url}
            return LeafNode("a", text_node.text, props)
        elif text_node.text_type == TextType.IMAGE:
            props = {"src": text_node.url, "alt": text_node.alt}
            return LeafNode("img", "", props)
        else:
            raise Exception("Need valid TextType")
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("Leaf nodes must have a value")
        elif not self.tag:
            return f"{self.value}"
        else:
            props_html = self.props_to_html()
            return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("needs Tag")
        elif self.children == None:
            raise ValueError("self.children missing value")
        else:
            chi = f""
            for child in self.children:
                chi += f"{child.to_html()}"
            return f"<{self.tag}>{chi}</{self.tag}>"