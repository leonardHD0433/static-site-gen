def markdown_to_blocks(markdown):
    block_list = markdown.split("\n\n")
    filtered_block_list = []
    for i in range(len(block_list)):
        stripped_block = block_list[i].strip()
        if block_list[i] != "":
            filtered_block_list.append(stripped_block)
    return filtered_block_list

