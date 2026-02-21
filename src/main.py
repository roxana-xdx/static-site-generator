from textnode import TextType, TextNode

def main():
    print("Hello world!")
    node = TextNode("Hello", TextType.BOLD, "https://www.boot.dev")
    print(node)

if __name__ == "__main__":
    main()
