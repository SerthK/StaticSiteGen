from textnode import TextNode, TextType

def main():
    testNode = TextNode("asdf", TextType.BOLD, "https://www.boot.dev")
    testNode2 = TextNode("asdf", TextType.NORMAL)
    print(testNode.__repr__())
    print(testNode2.__repr__())

if __name__ == "__main__":
    main()