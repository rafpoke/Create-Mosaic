from PIL import Image, ImageOps

def create_image_mosaic(input_path, output_path, in_image, rows, cols):
    # Load the original image
    original = Image.open(input_path)
    width, height = original.size

    # compress the mosaic tile
    red_factor = 10 # image compression factor

    red_width = round(width/red_factor)
    red_height = round(height/red_factor)
    reduced = original.resize((red_width, red_height)).convert("L")

    # Create a new image with the desired size
    mosaic = Image.new('RGB', (red_width * cols, red_height * rows))

    

    # Paste the image in a grid
    for row in range(rows):
        for col in range(cols):
            x = col * red_width
            y = row * red_height

            # extract color from the pixel in the input image
            rgb = compressed.getpixel((col, row))
            colorized = ImageOps.colorize(reduced, black="black", white=rgb)
            mosaic.paste(colorized, (x, y))

    # Save the final image as JPEG
    mosaic.save(output_path, format='JPEG')
    print(f"Mosaic saved to {output_path}")

# define the image names and paths
input_image = <INPUT_IMAGE_PATH>
base_image = <TILE_IMAGE_PATH>
out_image = <OUTPUT_IMAGE_PATH>

# open the image that will be made into mosaic
og_enter = Image.open(input_image)
cols, rows = og_enter.size

# compressed the image to make the mosaic more clear
com_factor = 20
red_rows = round(rows/com_factor)
red_cols = round(cols/com_factor)
compressed = og_enter.resize((red_cols, red_rows)).convert("RGB")


# Call function and create the output image:
create_image_mosaic(base_image, out_image,compressed,  rows=red_rows, cols=red_cols)