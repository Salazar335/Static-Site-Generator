import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestTextNode(unittest.TestCase):

    def test_props_to_html(self):
        # Create an HTMLNode with some properties
        node = HTMLNode(
            "a", 
            "Click me", 
            None, 
            {"href": "https://www.example.com", "target": "_blank"}
        )
        
        # Call the props_to_html method
        result = node.props_to_html()
        
        # Check if the result contains the expected attributes with leading spaces
        assert ' href="https://www.example.com"' in result
        assert ' target="_blank"' in result
        
        # Print a success message if the assertions pass
        print("Test passed!")

    def test_repr(self):
        node = HTMLNode(
            "a", 
            "Click me", 
            None, 
            {"href": "https://www.example.com", "target": "_blank"}
        )
        result = repr(node)
        
        # Check if the result contains the essential information
        assert "tag = a" in result
        assert "value = Click me" in result
        assert "children = None" in result
        assert "href" in result
        assert "target" in result
        assert "https://www.example.com" in result
        assert "_blank" in result
        
        print("Repr test passed!")

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

# Run the test when the file is executed directly
if __name__ == "__main__":
    unittest.main()