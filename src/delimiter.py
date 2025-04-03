from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    start = None
    end = None
    for old_node in old_nodes:
        text = old_node.text
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        else:
            # Process text nodes
            while delimiter in text:
                # Find the first opening and closing delimiter
                start = text.find(delimiter)
                end = text.find(delimiter, start + len(delimiter))
                
                # If no closing delimiter is found, raise an error
                if end == -1:
                    raise Exception("Incomplete delimiter detected")
                
                # Add the text before the delimiter as a normal text node
                if start > 0:
                    new_nodes.append(TextNode(text[:start], TextType.TEXT))
                
                # Add the text within the delimiters with the specified text type
                new_nodes.append(TextNode(text[start + len(delimiter):end], text_type))
                
                # Update the text to process the remainder after the closing delimiter
                text = text[end + len(delimiter):]

            if text != "":
                new_nodes.append(TextNode(text, TextType.TEXT))
    
    return new_nodes