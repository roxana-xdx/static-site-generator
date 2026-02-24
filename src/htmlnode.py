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
        if self.props is not None:
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

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        if self.tag is None:
            return self.value
        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("invalid HTML: no tag")
        if self.children is None or len(self.children) == 0:
            raise ValueError("invalid HTML: children missing")
        HTML_tag = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            HTML_tag += child.to_html()
        
        HTML_tag += f"</{self.tag}>"

        return HTML_tag
    
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
