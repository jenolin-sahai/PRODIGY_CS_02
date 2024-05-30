from PIL import Image
import random

def swapping_pixels(image):
    pixels = list(image.getdata())
    width, height = image.size
    random.shuffle(pixels)
    encrypted_image = Image.new(image.mode, (width, height))
    encrypted_image.putdata(pixels)
    return encrypted_image

def apply_math_operation(image, operation):
    pixels = list(image.getdata())
    width, height = image.size
    modified_pixels = []
    for pixel in pixels:
        if isinstance(pixel, int):
            modified_pixel = operation(pixel)
        else:
            modified_pixel = tuple(operation(value) for value in pixel)
        modified_pixels.append(modified_pixel)
    modified_image = Image.new(image.mode, (width, height))
    modified_image.putdata(modified_pixels)
    return modified_image

def main():
    input_image_path = r"C:\Users\Jeno\Downloads\Screenshot 2024-01-22 202409-compressed.jpg"
    image = Image.open(input_image_path)
    swapped_image = swapping_pixels(image)
    swapped_image_path = "swapped_image1.jpg"
    swapped_image.save(swapped_image_path)
    print(f"Swapped image saved to {swapped_image_path}")

    def increase_brightness(value):
        return min(value + 50, 255)
    
    brightened_image = apply_math_operation(image, increase_brightness)
    brightened_image_path = "brightened_image1.jpg"
    brightened_image.save(brightened_image_path)
    print(f"Brightened image saved to {brightened_image_path}")

if __name__ == "__main__":
    main()
