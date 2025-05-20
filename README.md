# Static Site Generator

A powerful Python-based static site generator that converts Markdown content into styled HTML pages. Perfect for blogs, documentation sites, or personal websites that need a simple and efficient publishing workflow.

![Example Site Preview](docs/images/tolkien.png)

## Features

- **Markdown to HTML Conversion**: Support for headings, paragraphs, code blocks, blockquotes, ordered and unordered lists
- **Rich Text Formatting**: Inline styling including bold, italic, code snippets, links, and images
- **Templating System**: Custom HTML templates with variable substitution
- **Recursive Directory Processing**: Automatically handles nested content directories
- **Static Asset Management**: Copies images, CSS, and other static files to output directory
- **GitHub Pages Deployment**: Built-in support for GitHub Pages paths
- **Local Development Server**: Integrated preview server for testing

## Project Structure

```
static-site-gen/
├── content/               # Markdown source files
│   ├── index.md           # Homepage content
│   ├── blog/              # Blog articles
│   └── ...                # Other content sections
├── static/                # Static assets
│   ├── images/            # Image files
│   └── index.css          # Main stylesheet
├── template.html          # HTML template with placeholders
├── docs/                  # Generated site (for GitHub Pages)
├── src/                   # Source code
├── test/                  # Unit tests
├── main.sh                # Local development script
└── build.sh               # GitHub Pages deployment script
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/static-site-gen.git
   cd static-site-gen
   ```

2. No additional dependencies required! The generator uses standard Python libraries.

## Usage

### Local Development

To generate the site and start a local development server:

```bash
./main.sh
```

This will:
1. Generate the site from markdown in the `content` directory
2. Copy static assets from `static` to the output directory
3. Start a local server at http://localhost:8888

### GitHub Pages Deployment

To build the site for GitHub Pages:

```bash
./build.sh
```

This will generate the site with the correct base path for GitHub Pages hosting.

[Example Github Page](https://leonardhd0433.github.io/static-site-gen/)

## Content Creation

### Creating Pages

Pages are written in Markdown and stored in the `content` directory:

```markdown
# Page Title

This is a paragraph with **bold** and _italic_ text.

## Subheading

- List item 1
- List item 2

[Link Text](https://example.com)
```

### Page Structure

Each markdown file should start with an H1 heading that will be used as the page title:

```markdown
# Page Title

Content goes here...
```

### Directory Structure

The output structure matches your content directory structure:
- `content/about.md` → `docs/about.html`
- `content/blog/post.md` → `docs/blog/post.html`

## Customization

### Template

Edit `template.html` to change the overall HTML structure. Use these placeholders:
- `{{ Title }}` - Will be replaced with the H1 heading from your markdown
- `{{ Content }}` - Will be replaced with the HTML content generated from markdown

### Styling

Edit `static/index.css` to customize the styling of your generated site.

## Development

### Code Structure

- `src/markdown_to_htmlnode.py`: Core markdown to HTML conversion
- `src/generate_pages_recursive.py`: Handles directory traversal and page generation
- `src/text_to_textnodes.py`: Parses inline markdown formatting
- `src/block_to_blocktype.py`: Identifies markdown block types
- `src/htmlnode.py`, `src/parentnode.py`, `src/leafnode.py`: HTML node structure

### Testing

Run the test suite with:

```bash
./test.sh
```

## License

MIT License

## Acknowledgements

This project was created as part of the [Build a Static Site Generator course](https://www.boot.dev/courses/build-static-site-generator-python) from [Boot.dev](https://www.boot.dev).
