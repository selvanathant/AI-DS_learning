import cairosvg

# Convert SVG URL to PNG file
cairosvg.svg2png(
    url="https://upload.wikimedia.org/wikipedia/commons/0/02/Stack_Overflow_logo.svg",
    write_to="stack.png"
)
print("SVG converted to PNG successfully!")
