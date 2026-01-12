from mdsvg import create_precise_wrapper, render
from mdsvg import FontMeasurer, create_precise_wrapper
# pip install markdown-svg

# use precise text wrapping
measurer = FontMeasurer.system_default()
width = measurer.measure("Hello " , font_size=14)
wrap = create_precise_wrapper(max_width=30, font_size=14, measurer=measurer)
lines = wrap("Long text that needs accurate wrapping...")
# Render markdown to SVG
svg = render("""
# Hello World Hello World Hello World Hello World Hello World Hello World

This is a paragraph with **bold** and *italic* text.

- Item one
- Item two
- Item three
""")

# Save to file
with open("output.svg", "w") as f:
    f.write(svg)