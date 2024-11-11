import unittest

from leafnode import LeafNode

class LeafTestNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("a", "Click here!", {"href": "https://www.google.com", "target": "_blank"})
        node2 = LeafNode("a", "Click here!", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node, node2)

    def test_eq_noprops(self):
        node = LeafNode("p", "Click here!")
        node2 = LeafNode("p", "Click here!")
        self.assertEqual(node, node2)

    def test_to_html(self):
        node = LeafNode("p", "Click here!")
        html_string = "<p>Click here!</p>"
        self.assertEqual(html_string, node.to_html())

    def test_to_html_props(self):
        node = LeafNode("a", "Click here!", {"href": "https://www.google.com"})
        html_string = '<a href="https://www.google.com">Click here!</a>'
        self.assertEqual(html_string, node.to_html())

    def test_to_html_error(self):
        with self.assertRaises(ValueError):
            node = LeafNode("a", None, {"href": "https://www.google.com"})
            node.to_html()

if __name__ == "__main__":
    unittest.main()