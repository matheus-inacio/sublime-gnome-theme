from PIL import Image, ImageDraw

def make_tab(width, height, radius, filename):
    im = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(im)
    
    # Draw rounded top corners
    draw.pieslice([0, 0, radius*2, radius*2], 180, 270, fill=(255, 255, 255, 255))
    draw.pieslice([width - radius*2, 0, width, radius*2], 270, 360, fill=(255, 255, 255, 255))
    
    # Draw rectangles to fill the rest
    draw.rectangle([radius, 0, width - radius, radius], fill=(255, 255, 255, 255))
    draw.rectangle([0, radius, width, height], fill=(255, 255, 255, 255))
    
    im.save(filename)

make_tab(48, 48, 8, "GNOME Dark/assets/tabs/tab_mask.png")
make_tab(96, 96, 16, "GNOME Dark/assets/tabs/tab_mask@2x.png")
