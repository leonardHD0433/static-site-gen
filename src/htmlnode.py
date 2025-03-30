class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.__children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html_string = ""
        if self.props:  # Automatically handles both `None` and empty `{}` gracefully
            for prop, value in self.props.items():  # Dictionary unpacking for readability
                html_string += f" {prop}=\"{value}\""
        return html_string
    
    def children_getter(self):
        return self.__children
    
    def __repr__(self):
        return f"\nTag: {self.tag}\nValue: {self.value}\nChildren: {self.__children}\nProps: {self.props}"