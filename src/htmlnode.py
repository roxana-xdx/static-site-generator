class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag # e.g. "p", "a", "h1", etc.
        self.value = value # e.g. text inside a paragraph
        self.children = children # list of HTMLNode objects, children of this node
        self.props = props # dictionary with the attributes of the HTML tag, e.g. <a> might have {"href": "https://www.google.com"}

    def to_html(self):
        raise NotImplementedError("to_html method not implemented") # child classes override this method

    def props_to_html(self):
        attributes = ""
        for key, value in self.props.items():
            attributes += f" {key}=\"{value}\""
        return attributes
    
    def __eq__(self, other):
        return (self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
