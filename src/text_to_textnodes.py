from textnode import TextType, TextNode
from delimiter import split_nodes_delimiter
from split_node import split_nodes_image, split_nodes_link

def text_to_textnodes(text):
    node = [TextNode(text, TextType.TEXT)]
    # split bold
    node = split_nodes_delimiter(node, "**", TextType.BOLD)
    # split italic
    node = split_nodes_delimiter(node, "_", TextType.ITALIC)
    # split code
    node = split_nodes_delimiter(node, "`", TextType.CODE)
    # split image
    node = split_nodes_image(node)
    # split link
    node = split_nodes_link(node)

    return node



