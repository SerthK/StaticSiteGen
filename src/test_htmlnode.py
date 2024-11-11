import unittest

from htmlnode import HTMLNode

class HTMLTestNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a", "Click here!", None, {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("a", "Click here!", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node, node2)

    def test_noteq_tag(self):
        node = HTMLNode("p", "Click here!", None, {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("a", "Click here!", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertNotEqual(node, node2)

    def test_noteq_value(self):
        node = HTMLNode("a", "Click here!", None, {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("a", "Click hereeeeeeee!", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertNotEqual(node, node2)

    def test_noteq_children(self):
        node = HTMLNode("a", "Click here!", ["asdf", "asdf2"], {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("a", "Click here!", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertNotEqual(node, node2)

    def test_noteq_props(self):
        node = HTMLNode("a", "Click here!", None, {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("a", "Click here!", None, {"href": "https://www.googleeeeeeee.com", "target": "_blank"})
        self.assertNotEqual(node, node2)


    def test_props_to_html(self):
        props_string = ' href="https://www.google.com" target="_blank"'
        node = HTMLNode("a", "Click here!", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(props_string, node.props_to_html())

if __name__ == "__main__":
    unittest.main()