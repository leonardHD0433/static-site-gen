def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            title = line[2:].strip()
            break
    else:
        raise Exception("Title not found.")
    
    return title

