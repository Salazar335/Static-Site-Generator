from textnode import TextNode, TextType

def main():
    node = TextNode("Some example text", TextType.links, "https://example.com")
    print(node)

if __name__ == "__main__":
    main()