from mardown_to_blocks import markdown_to_blocks
from block_to_blocktype import block_to_block_type
from text_to_textnodes import text_to_textnodes
from text_to_html import text_node_to_html_node
from parentnode import ParentNode
from leafnode import LeafNode
from block_type import BlockType

"""
    Converts a full markdown document into a single root ParentNode ("div") 
    that contains child HTMLNodes (one for each markdown block).
"""
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown) # Step 1: Split markdown into blocks (paragraphs, headers, etc.)
    children_nodes = [] # List to collect the HTMLNodes for each block

    # Step 2: Process each block
    for block in blocks:
        block_type = block_to_block_type(block) # Determine block type
        block = block.replace("\n", " ") # Replace newlines with spaces
        text_nodes = text_to_textnodes(block) # Parse text into TextNode objects for inline styles
        html_nodes = create_HTMLNodes(text_nodes) # Convert text nodes to html nodes

        # Add the HTMLNode for this block (using the proper tag) to the list of children
        children_nodes.append(add_tag_to_block(html_nodes, block_type)) 

    # Step 3: Wrap all block nodes inside one root <div> and return the tree
    return ParentNode("div", children=children_nodes)

"""
    Helper function - converts a list of TextNode objects
    into HTMLNode objects using text_node_to_html_node.
"""
def create_HTMLNodes(text_nodes):
    html_nodes = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        html_nodes.append(html_node)
    return html_nodes

"""
    Helper function - wraps a list of HTMLNode children in the correct ParentNode or LeafNode
    depending on the markdown block type.
    Only PARAGRAPH currently uses Proper Node logic; other types still use strings (to be improved).
"""
def add_tag_to_block(html_nodes, block_type):
    if block_type == BlockType.PARAGRAPH:
        return ParentNode("p", children=html_nodes)
    if block_type == BlockType.HEADING:
        html = f"<p>{html}</p>"
    if block_type == BlockType.CODE:
        html = f"<p>{html}</p>"    
    if block_type == BlockType.QUOTE:
        html = f"<blockquote>{html}</blockquote>"
    if block_type == BlockType.ORDERED_LIST:
        html = f"<p>{html}</p>"
    if block_type == BlockType.UNORDERED_LIST:
        html = f"<p>{html}</p>"

    return html

    