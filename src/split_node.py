from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_node(old_nodes, extract_markdown, text_type):
    # return markdown text format of the given text type
    def markdown_format(alt, url):
        if text_type == TextType.IMAGE:
            return f"![{alt}]({url})"
        elif text_type == TextType.LINK:
            return f"[{alt}]({url})"

    new_nodes = []
    # For each node in the input list 
    for old_node in old_nodes:
        text = old_node.text
        markdown = extract_markdown(text)
        # Check if it contains the given markdown (✓)
        # If it does, extract the parts and create new nodes(✓)
        if markdown:
            current_text = text
            for alt, url in markdown:
                sections = current_text.split(markdown_format(alt, url), 1)

                if sections[0]:
                    new_nodes.append(TextNode(sections[0], old_node.text_type))

                new_nodes.append(TextNode(alt, text_type, url))
                
                if sections[1]:
                    current_text = sections[1]
                else:
                    current_text = ""
                    
            if current_text:
                new_nodes.append(TextNode(current_text, old_node.text_type))
        # If not, just add the original node to the result (✓)
        else:
            new_nodes.append(old_node)
    return new_nodes


def split_nodes_image(old_nodes):
    return split_node(old_nodes, extract_markdown_images, TextType.IMAGE)

def split_nodes_link(old_nodes):
    return split_node(old_nodes, extract_markdown_links, TextType.LINK)



        