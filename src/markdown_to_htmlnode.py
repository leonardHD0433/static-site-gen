from mardown_to_blocks import markdown_to_blocks
from block_to_blocktype import block_to_block_type
from text_to_textnodes import text_to_textnodes
from text_to_html import text_node_to_html_node
from delimiter import split_nodes_delimiter
from textnode import TextNode, TextType
from parentnode import ParentNode
from leafnode import LeafNode
from block_type import BlockType

"""
    Converts a full markdown document into a single root ParentNode ("div") 
    that contains child HTMLNodes (one for each markdown block).
"""
def markdown_to_html_node(markdown):
    #print(repr(markdown))
    blocks = markdown_to_blocks(markdown) # Step 1: Split markdown into blocks (paragraphs, headers, etc.)
    children_nodes = [] # List to collect the HTMLNodes for each block

    # Step 2: Process each block
    for block in blocks:
        block_type = block_to_block_type(block) # Determine block type
        # Add the HTMLNode for this block (using the proper tag) to the list of children
        children_nodes.append(add_tag_to_block(block, block_type)) 

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
def add_tag_to_block(block, block_type):
    html_nodes = []
    if block_type == BlockType.PARAGRAPH:
        text_nodes = text_to_textnodes(block) # Parse text into TextNode objects for inline styles
        html_nodes = create_HTMLNodes(text_nodes) # Convert text nodes to html nodes
        for html_node in html_nodes:
            html_node.value = html_node.value.replace("\n", " ") # Replace newlines with spaces
        return ParentNode("p", children=html_nodes)
    
    if block_type == BlockType.HEADING:
        heading_count = 0
        heading_string = ""
        for char in block:
            if char == "#":
                heading_count += 1
                heading_string += "#"
            else:
                break
        heading_content = block.lstrip(f"{heading_string} ")
        text_nodes = text_to_textnodes(heading_content)
        html_node = create_HTMLNodes(text_nodes)
        return ParentNode(f"h{heading_count}", children= html_node)
    
    if block_type == BlockType.CODE:
        block = block.replace("```", "").lstrip("\n")
        text_node = TextNode(block, TextType.TEXT)
        html_node = create_HTMLNodes([text_node])
        return ParentNode("pre", children=[ParentNode("code", children = html_node)])   
    
    if block_type == BlockType.QUOTE:
        lines = block.split("\n")
        cleaned_lines = []
        for line in lines:
            cleaned_lines.append(line.lstrip(">").strip())
        cleaned_block = " ".join(cleaned_lines).strip().replace("  ", "\n\n")
        text_nodes = text_to_textnodes(cleaned_block)
        html_nodes = create_HTMLNodes(text_nodes)
        return ParentNode("blockquote", children=html_nodes)
    
    if block_type == BlockType.ORDERED_LIST:
        item_list_nodes = []
        item_list = block.split("\n")
        for i in range(len(item_list)):
            cleaned_item = (item_list[i].lstrip(f"{i + 1}. ").strip())
            text_node = text_to_textnodes(cleaned_item)
            html_node = create_HTMLNodes(text_node)
            item_list_nodes.append(ParentNode("li", children=html_node))
        return ParentNode("ol", children=item_list_nodes)

    if block_type == BlockType.UNORDERED_LIST:
        item_list_nodes = []
        item_list = block.split("\n")
        for item in item_list:
            cleaned_item = (item.lstrip("- ").strip())
            text_node = text_to_textnodes(cleaned_item)
            html_node = create_HTMLNodes(text_node)
            item_list_nodes.append(ParentNode("li", children=html_node))
        return ParentNode("ul", children=item_list_nodes)