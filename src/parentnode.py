from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError()
        elif self.children_getter() is None:
            raise ValueError("Y no children?")
        
        html_string = f"<{self.tag}"
        if self.props:
            html_string += self.props_to_html()
        html_string += ">"

        for child in self.children_getter():
            html_string += child.to_html()

        return html_string + f"</{self.tag}>"
                
