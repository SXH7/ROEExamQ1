from markitdown import MarkItDown

md = MarkItDown(enable_plugins=False) # Set to True to enable plugins
result = md.convert("q-pdf-to-markdown.pdf")
print(result.text_content)