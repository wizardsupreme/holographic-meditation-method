import os
from PIL import Image, ImageDraw # type: ignore

def ensure_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def create_base_image(size, bg_color="#6B46C1"):
    """Create a base image with infinity symbol"""
    # Create a circular mask
    mask = Image.new('L', (size, size), 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.ellipse((0, 0, size, size), fill=255)
    
    # Create the base image with transparency
    image = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    # Create a circular background
    bg = Image.new('RGBA', (size, size), bg_color)
    image.paste(bg, (0, 0), mask)
    
    draw = ImageDraw.Draw(image)
    
    # Calculate dimensions for the infinity symbol
    padding = size * 0.2  # 20% padding
    symbol_width = size - (2 * padding)
    symbol_height = symbol_width * 0.4
    
    # Center position
    center_x = size / 2
    center_y = size / 2
    
    # Draw infinity symbol (simplified version with circles)
    circle_radius = symbol_height / 2
    left_center = (center_x - circle_radius, center_y)
    right_center = (center_x + circle_radius, center_y)
    
    # Draw two circles in white
    draw.ellipse([
        left_center[0] - circle_radius,
        left_center[1] - circle_radius,
        left_center[0] + circle_radius,
        left_center[1] + circle_radius
    ], outline='white', width=max(1, int(size * 0.05)))
    
    draw.ellipse([
        right_center[0] - circle_radius,
        right_center[1] - circle_radius,
        right_center[0] + circle_radius,
        right_center[1] + circle_radius
    ], outline='white', width=max(1, int(size * 0.05)))
    
    return image

def generate_favicons(output_dir):
    """Generate all required favicon files"""
    ensure_directory(output_dir)
    
    # Sizes needed for different platforms
    sizes = {
        'favicon-16x16.png': 16,
        'favicon-32x32.png': 32,
        'apple-touch-icon.png': 180,
        'android-chrome-192x192.png': 192,
        'android-chrome-512x512.png': 512
    }
    
    # Generate PNGs
    favicon_images = {}
    for filename, size in sizes.items():
        output_path = os.path.join(output_dir, filename)
        img = create_base_image(size)
        img.save(output_path, 'PNG')
        favicon_images[size] = img
    
    # Generate ICO file (contains both 16x16 and 32x32)
    ico_path = os.path.join(output_dir, 'favicon.ico')
    favicon_images[16].save(
        ico_path,
        format='ICO',
        sizes=[(16, 16), (32, 32)],
        append_images=[favicon_images[32]]
    )

if __name__ == "__main__":
    # Get the absolute path to the project root
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(project_root, 'static', 'favicon')
    
    generate_favicons(output_dir)
    print("Favicon generation complete!") 