from PIL import Image, ImageDraw

def make_pill(width, height, radius, padding, filename):
    im = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(im)
    
    # Calculate pill coordinates
    x0 = padding
    y0 = padding
    x1 = width - padding
    y1 = height - padding
    
    # Draw pill
    draw.rounded_rectangle([x0, y0, x1, y1], radius=radius, fill=(255, 255, 255, 255))
    
    im.save(filename)

# For 1x: 32x32 image, 4px padding, 6px radius. Inner margin will be padding + radius = 10.
make_pill(32, 32, 6, 4, "GNOME Dark/assets/tabs/tab_pill.png")
# For 2x: 64x64 image, 8px padding, 12px radius.
make_pill(64, 64, 12, 8, "GNOME Dark/assets/tabs/tab_pill@2x.png")
