class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        attributes = ''.join([f' {key}="{value}"' for key, value in self.props.items()])
        return attributes

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def __eq__(self, targetHTMLNode):
        return (
            self.tag == targetHTMLNode.tag and
            self.value == targetHTMLNode.value and
            self.children == targetHTMLNode.children and
            self.props == targetHTMLNode.props
        )