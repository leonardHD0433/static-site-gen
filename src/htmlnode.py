class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html_string = ""
        if self.props != None: 
            for prop in self.props:
                html_string += f" {prop}=\"{self.props[prop]}\""
        return html_string
    
    def __repr__(self):
        return f"\nTag: {self.tag}\nValue: {self.value}\nChildren: {self.children}\nProps: {self.props}"