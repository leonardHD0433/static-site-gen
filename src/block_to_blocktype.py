from block_type import BlockType

def block_to_block_type(markdown):
    lines = markdown.split("\n")
    # Check for heading block
    if markdown.startswith("#"):
        heading_count = 0
        for char in markdown:
            if char == "#":
                heading_count += 1
            else:
                break
        if 1 <= heading_count <= 6 and markdown[heading_count] == " ":
            return BlockType.HEADING
    
    # Check for code block
    if markdown.startswith("```") and markdown.endswith("```"):
        return BlockType.CODE
    
    # Check for quote block
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    
    # Check for unordered_list block
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    
    # Check for ordered_list block
    if len(lines) > 0:
        is_ordered = True
        for i in range(0, len(lines)):
            if not lines[i].startswith(f"{i+1}. "):
                is_ordered = False
                break
        if is_ordered:
            return BlockType.ORDERED_LIST

    # If no conditions met, return paragraph block
    return BlockType.PARAGRAPH
