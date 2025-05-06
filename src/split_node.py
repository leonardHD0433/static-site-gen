from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    new_nodes = []
    # For each node in the input list (✓)
    for old_node in old_nodes:
        text = old_node.text
        images = extract_markdown_images(text)
        # Check if it contains an image markdown
        # If it does, extract the parts and create new nodes
        if images:
            current_text = text
            for image_alt, image_url in images:
                sections = current_text.split(f"![{image_alt}]({image_url})", 1)

                if sections[0]:
                    new_nodes.append(TextNode(sections[0], old_node.text_type))

                new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))
                
                if sections[1]:
                    current_text = sections[1]
                else:
                    current_text = ""
                    
            if current_text:
                new_nodes.append(TextNode(current_text, old_node.text_type))
        # If not, just add the original node to the result
        else:
            new_nodes.append(old_node)
    return new_nodes

def split_nodes_link(old_nodes):
    pass