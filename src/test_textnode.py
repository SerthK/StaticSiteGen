import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_false_TextType(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false_Text(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        node2 = TextNode("This is a text node2", TextType.NORMAL)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_uneq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boots.dev")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("asdf", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("testerino", TextType.NORMAL)
        self.assertEqual(node.__repr__(), "TextNode(asdf, bold, https://www.boot.dev)")
        self.assertEqual(node2.__repr__(), "TextNode(testerino, normal, None)")



if __name__ == "__main__":
    unittest.main()